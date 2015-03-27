from flask import Flask, render_template
from pattern.web import Twitter

app = Flask(__name__)


@app.route('/')
def hello_world():
    t = Twitter()
    return render_template('simpleui.html', my_list=t.trends())

@app.route('/components.html')
def hello_world():
    t = Twitter()
    return render_template('simpleui.html', my_list=t.trends())

@app.route('/')
def hello_world():
    t = Twitter()
    return render_template('simpleui.html', my_list=t.trends())

@app.route('/')
def hello_world():
    t = Twitter()
    return render_template('simpleui.html', my_list=t.trends())

@app.route('/')
def hello_world():
    t = Twitter()
    return render_template('simpleui.html', my_list=t.trends())

if __name__ == '__main__':
    app.run()
