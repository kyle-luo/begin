from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from config import Config

app = Flask(__name__, template_folder='../templates')
bs = Bootstrap(app)
db = SQLAlchemy(app)

app.config.from_object(Config)

@app.route('/')

# def go():
#     title = 'render template'
#     p = ['lao da', 'lao er', 'lao san']
#     # return render_template('render templates.html')
#     # return render_template('render templates.html', title=title)
#     return render_template('render templates.html', title=title, data=p)

def run():
    return render_template('nav.html')


if __name__ == '__main__':
    app.run(debug=True, port=2000)