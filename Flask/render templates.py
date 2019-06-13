from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bs = Bootstrap(app)


@app.route('/')

def go():
    title = 'render template'
    p = ['lao da', 'lao er', 'lao san']
    # return render_template('render templates.html')
    # return render_template('render templates.html', title=title)
    return render_template('render templates.html', title=title, data=p)

if __name__ == '__main__':
    app.run(debug=True)