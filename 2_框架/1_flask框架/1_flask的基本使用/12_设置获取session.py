# coding:utf8
from flask import Flask, session, redirect, url_for

app = Flask(__name__)
# 注意设置session的时候必须设置app.secret_key
app.secret_key = "aaa"

@app.route('/index1')
def index1():
    session['username'] = 'itcast'
    return redirect(url_for('index'))

@app.route('/')
def index():
    return session.get('username')

if __name__ == '__main__':
    app.run(debug=True)