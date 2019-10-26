# coding:utf8

from flask import Flask,redirect

app = Flask(__name__)


@app.route('/')
def deomo():
    return redirect('http://www.baidu.com')

if __name__ == '__main__':
    app.run(debug=True)