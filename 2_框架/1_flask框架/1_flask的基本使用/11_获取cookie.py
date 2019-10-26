#coding:utf8

from flask import Flask,make_response,request

app = Flask(__name__)


@app.route('/cookie')
def set_cookie():
    response = make_response('cookie设置成功')
    response.set_cookie("name", 'zhang')
    return response

@app.route('/getcookie')
def get_cookie():
    res = request.cookies.get("name")
    return res

if __name__ == '__main__':
    app.run(debug=True)