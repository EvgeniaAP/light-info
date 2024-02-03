import _locale
import math

from flask import Flask, render_template, request

from utils.db_connection import DBConnection
from utils.models import Formula, Theorema, Figure

_locale._getdefaultlocale = (lambda *args: ['en_US', 'utf8'])

app = Flask(__name__)
connection = DBConnection(app)

connection.connect()


connection.create_tables()
connection.create_demo_data()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/search', methods=['GET'])
def search():
    return connection.search_theory(request.args['text'])


@app.route('/figure/', methods=['GET'])
def figure_list():
    page = int(request.args['page']) if 'page' in request.args else 1
    size = 6
    rang_p = math.ceil(connection.get_count(Figure) / size)

    return render_template("list-page.html", title='Фигуры', items=connection.get_figures(page, size), page=page, size=range(rang_p))

@app.route('/figure/plain/', methods=['GET'])
def figure_list_plain():
    page = int(request.args['page']) if 'page' in request.args else 1
    size = 6
    rang_p = math.ceil(connection.get_plain_fig_count() / size)

    return render_template("list-page.html", title='Фигуры  / Планиметрия', items=connection.get_plain_figures(page, size), page=page, size=range(rang_p))


@app.route('/figure/stereo/', methods=['GET'])
def figure_list_stereo():
    page = int(request.args['page']) if 'page' in request.args else 1
    size = 6
    rang_p = math.ceil(connection.get_stereo_fig_count() / size)

    return render_template("list-page.html", title='Фигуры  / Стереометрия', items=connection.get_stereo_figures(page, size), page=page, size=range(rang_p))


@app.route('/figure/<id>', methods=['GET'])
def figure(id: int):
    return render_template("figure.html", figure=connection.get_by_id(id, Figure))

@app.route('/formula/<id>', methods=['GET'])
def formula(id: int):
    return render_template("formula.html", formula=connection.get_by_id(id, Formula))


@app.route('/formula/', methods=['GET'])
def formula_list():
    page = int(request.args['page']) if 'page' in request.args else 1
    size = 6
    rang_p = math.ceil(connection.get_count(Formula) / size)

    return render_template("list-page.html", title='Формулы', items=connection.get_formuls(page, size), page=page, size=range(rang_p))

@app.route('/theorema/<id>', methods=['GET'])
def theorema(id: int):
    return render_template("theorema.html", theorema=connection.get_by_id(id, Theorema))


@app.route('/theorema/', methods=['GET'])
def theorema_list():
    page = int(request.args['page']) if 'page' in request.args else 1
    size = 6
    rang_p = math.ceil(connection.get_count(Theorema) / size)

    return render_template("list-page.html", title='Теоремы', items=connection.get_theorema(page, size), page=page, size=range(rang_p))


if __name__ == '__main__':
    app.run(debug=True)
