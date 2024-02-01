import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, text
from sqlalchemy.orm import DeclarativeBase, lazyload, joinedload
from sqlalchemy.orm.collections import InstrumentedList

from utils.models import BaseModel, Figure, Formula, Theorema, Feature


class Dict:
    id: int
    name: str
    source: str

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    def to_dict(self) -> dict:
        return self.__dict__

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
            fig1 = Figure(name='Figure 1', info='Figure 1 info')
            fig2 = Figure(name='Figure 2', info='Figure 2 info')
            form1 = Formula(name='Formula 1', latex="\\documentclass[14pt]{book} \\begin{document} $ f(x) = \\int_{-\\infty}^\\infty \\hat f(\\xi)\,e^{2 \\pi i \\xi x} \\, d\\xi $ \\end{document}")
            form2 = Formula(name='Formula 2')
            theorema = Theorema(name='Theorema\'la 1')
            feat1 = Feature(text='Feature 1', formula=form1, figure=fig1)





            self.db.session.add_all([fig1, fig2, form1, form2, theorema, feat1, self.sqr(), self.cube()])
            self.db.session.commit()

    def sqr(self):
        sqrText = 'Квадра́т (от лат. quadratus, четырёхугольный) — правильный четырёхугольник, то есть плоский четырёхугольник, у которого все углы и все стороны равны. Каждый угол квадрата — прямой ( 90 ∘ ).'
        sqrText += ' Квадрат может быть однозначно охарактеризован разными способами. \n * Четырёхугольник, диагонали которого равны и взаимно перпендикулярны, причём точка пересечения делит их пополам. \n * Четырёхугольник, являющийся одновременно прямоугольником и ромбом. \n * Прямоугольник, у которого длины двух смежных сторон равны. \n * Прямоугольник, у которого диагонали пересекаются под прямым углом. \n * Ромб, у которого диагонали равны. \n * Ромб, у которого два соседних угла равны. \n * Ромб, один из углов которого — прямой (прочие углы, как легко доказать, тогда также прямые). \n * Параллелограмм, у которого длины двух смежных сторон равны, а угол между ними — прямой. \n * Параллелограмм, у которого диагонали равны, а угол между ними — прямой. \n * Дельтоид, все углы которого прямые.'

        baseImg = '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'
        sf1 = 'Диагонали квадрата равны, взаимно перпендикулярны, делятся точкой пересечения пополам и сами делят углы квадрата пополам (другими словами, являются биссектрисами внутренних углов квадрата).'
        sff1 = '\\documentclass[14pt]{book} \\begin{document}  $ d = a \sqrt{2} $ \end{document}'

        sqrFf = Formula(name='Площадь квадрата', latex=sff1)
        sqrf = Feature(text=sf1, formula=sqrFf)
        sqrf2 = Feature(text='Периметр квадрата равен', formula=Formula(name='Периметр квадрата ',
                                                                        latex='\\documentclass[14pt]{book} \\begin{document}  $ P = 4 a = 4 \sqrt{2} R = 8 r $ \end{document}'))

        sqr = Figure(name='Квадрат', info=sqrText, image=baseImg, plain=True, features=[sqrf, sqrf2])

        return sqr

    def cube(self):
        text = 'Куб (др.-греч. κύβος[1]); иногда гекса́эдр[2][3] или правильный гекса́эдр[4][5] — многогранник, поверхность которого состоит из шести квадратов. Куб является правильным многогранником. Частный случай параллелепипеда и призмы. В различных дисциплинах используются значения термина, имеющие отношения к тем или иным свойствам геометрического прототипа. В частности, в аналитике (OLAP-анализ) применяются так называемые аналитические многомерные кубы, позволяющие в наглядном виде сопоставить данные из различных таблиц.'


        return  Figure(name='Куб', info=text, image='cube', plain=False)

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

    def get_figure_by_id(self, id: int) -> Figure | None:
        with self.app.app_context():
            result = select(Figure).where(Figure.id == id)
            for figure in self.db.session.scalars(result):
                c = figure.features
                return figure
        return None