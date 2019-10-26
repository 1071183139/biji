#coding:utf8
from flask import Flask, redirect, url_for


app = Flask(__name__)


@app.route('/')
def set_cookie():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return '张'

if __name__ == '__main__':
    app.run(debug=True)