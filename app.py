import _locale

from flask import Flask, render_template, request

from utils.db_connection import DBConnection

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

@app.route('/figure/<id>', methods=['GET'])
def figure(id: int):
    return render_template("figure.html", figure=connection.get_figure_by_id(id))

if __name__ == '__main__':
    app.run(debug=True)
