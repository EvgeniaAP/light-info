import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, text
from sqlalchemy.orm import DeclarativeBase, query

from utils.models.models import BaseModel, Figure


class Dict:
    id: int
    name: str


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
            self.db.drop_all()
            BaseModel.metadata.create_all(self.db.engine)

    def set_up_uri(self):
        self.app.config['SQLALCHEMY_DATABASE_URI'] =  self.connection_uri()

    def connection_uri(self) -> str:
        return f'postgresql+psycopg2://{self.user}:{self.password}@127.0.0.1:5432/{self.db_name}'


    def search_theory(self, textStr: str) -> list[Dict]:
        result = []
        with self.app.app_context():
            session = self.db.session
            figures = select(Figure).from_statement(text(f'select * from figure where figure.name LIKE \'%{textStr}%\''))

            for figure in session.scalars(figures):
                result.append(figure)

        print(result, '!')

        return result