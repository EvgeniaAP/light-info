import _locale

from flask import Flask, render_template

from utils.db_connection import DBConnection

_locale._getdefaultlocale = (lambda *args: ['en_US', 'utf8'])

app = Flask(__name__)
connection = DBConnection(app)

connection.connect()


connection.create_tables()

connection.search_theory('')

@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


if __name__ == '__main__':

    app.run(debug=True)
