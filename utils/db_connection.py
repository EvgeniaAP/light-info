import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, text
from sqlalchemy.orm import DeclarativeBase, lazyload, joinedload
from sqlalchemy.orm.collections import InstrumentedList

from utils.migrations import Migrations
from utils.models import BaseModel, Figure, Formula, Theorema, Feature


class Dict:
    id: int
    name: str
    source: str

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    def to_dict(self) -> dict:
        return self.__dict__

class ListItem:
    id:int
    name: str
    category: str
    sub_category: str
    info: str
    link: str

class DBConnection:
    user: str
    password: str
    db_name: str
    app: Flask
    db: SQLAlchemy

    def __init__(self, app: Flask):
        json_env = json.load(open('utils/.env', encoding='utf-8'))
        self.user = json_env['sql_user']
        self.password = json_env['sql_password']
        self.db_name = json_env['sql_db_name']
        self.app = app

    def connect(self):
        self.set_up_uri()
        self.db = SQLAlchemy(self.app, model_class=DeclarativeBase)

    def create_tables(self):
        with self.app.app_context():
            self.clear_data()
            BaseModel.metadata.create_all(self.db.engine)
            self.db.session.commit()

    def create_demo_data(self):
        with self.app.app_context():
            demo = Migrations().load_v1(self.app, self.db)

            self.db.session.add_all(demo)
            self.db.session.commit()

    def clear_data(self):
        session = self.db.session
        meta = BaseModel.metadata
        for table in reversed(meta.sorted_tables):
            table.drop(bind=self.db.engine, checkfirst=True)
            session.commit()


    def set_up_uri(self):
        self.app.config['SQLALCHEMY_DATABASE_URI'] =  self.connection_uri()

    def connection_uri(self) -> str:
        return f'postgresql+psycopg2://{self.user}:{self.password}@127.0.0.1:5432/{self.db_name}'


    def map_to_dict(self, model: BaseModel) -> Dict:
        obj = Dict()
        obj.id = model.id
        obj.name = model.name
        obj.source = model.__table__.fullname
        return obj

    def search_theory(self, textStr: str) -> list[dict]:
        result = []
        with self.app.app_context():
            session = self.db.session
            figures = select(Figure).from_statement(text(f'select id, name from figure where LOWER(name) LIKE LOWER(\'%{textStr}%\')'))

            for figure in session.scalars(figures):
                result.append(self.map_to_dict(figure))

            formulas = select(Formula).from_statement(text(f'select id, name from formula where LOWER(name) LIKE LOWER(\'%{textStr}%\')'))

            for formula in session.scalars(formulas):
                result.append(self.map_to_dict(formula))

            theoremas = select(Theorema).from_statement(text(f'select id, name from theorema where LOWER(name) LIKE LOWER(\'%{textStr}%\')'))

            for theorema in session.scalars(theoremas):
                result.append(self.map_to_dict(theorema))

        return json.dumps(list(map(lambda x: x.to_dict(), result)))

    def get_figures(self, page, size) -> list[ListItem]:
        results = []
        with self.app.app_context():
            for figure in self.db.session.query(Figure).offset((page-1)*size).limit(size).all():
                item = ListItem()
                item.id = figure.id
                item.name = figure.name
                item.info = figure.info[:180]+'...'
                item.category = 'Фигура'
                item.sub_category = 'Планиметрия' if figure.plain else 'Стереометрия'
                item.link = figure.__table__
                results.append(item)

        return results

    def get_plain_fig_count(self) -> int:
        with self.app.app_context():
            return self.db.session.query(Figure.id).where(Figure.plain==True).count()

    def get_plain_figures(self, page, size) -> list[ListItem]:
        results = []
        with self.app.app_context():
            for figure in self.db.session.query(Figure).where(Figure.plain==True).offset((page-1)*size).limit(size).all():
                item = ListItem()
                item.id = figure.id
                item.name = figure.name
                item.info = figure.info[:180]+'...'
                item.category = 'Фигура'
                item.sub_category = 'Планиметрия' if figure.plain else 'Стереометрия'
                item.link = figure.__table__
                results.append(item)

        return results


    def get_stereo_fig_count(self) -> int:
        with self.app.app_context():
            return self.db.session.query(Figure.id).where(Figure.plain==False).count()

    def get_stereo_figures(self, page, size) -> list[ListItem]:
        results = []
        with self.app.app_context():
            for figure in self.db.session.query(Figure).where(Figure.plain==False).offset((page-1)*size).limit(size).all():
                item = ListItem()
                item.id = figure.id
                item.name = figure.name
                item.info = figure.info[:180]+'...'
                item.category = 'Фигура'
                item.sub_category = 'Планиметрия' if figure.plain else 'Стереометрия'
                item.link = figure.__table__
                results.append(item)

        return results

    def get_count(self, klass) -> int:
        with self.app.app_context():
            return self.db.session.query(klass.id).count()

    def get_formuls(self, page, size) ->list[ListItem]:
        results = []
        with self.app.app_context():
            for formula in self.db.session.query(Formula).offset((page-1)*size).limit(size).all():
                item = ListItem()
                item.id = formula.id
                item.name = formula.name
                item.info = formula.description[:180]+'...' if formula.description else ''
                item.category = 'Формула'
                item.sub_category = ''
                item.link = formula.__table__
                results.append(item)

        return results

    def get_theorema(self, page, size) ->list[ListItem]:
        results = []
        with self.app.app_context():
            for thr in self.db.session.query(Theorema).offset((page-1)*size).limit(size).all():
                item = ListItem()
                item.id = thr.id
                item.name = thr.name
                item.info = thr.text[:180]+'...' if thr.text else ''
                item.category = 'Теорема'
                item.sub_category = ''
                item.link = thr.__table__
                results.append(item)

        return results

    def get_by_id(self, id: int, klass):
        with self.app.app_context():
            result = select(klass).where(klass.id == id)
            for f in self.db.session.scalars(result):
                if klass == Figure:
                    d = f.features
                if klass == Theorema:
                    d = f.formulas

                return f
        return None