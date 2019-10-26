# encoding=utf8
from flask import Flask, abort
app = Flask(__name__)

@app.route('/statecode')
def demo1():
    return 'statecode',666



@app.route('/notfind')
def demo2():
    abort(404)
    return '抛出404的异常'


# errorhandler 可以捕获http错误的状态码，还可以捕获指定的异常
@app.errorhandler(404)
def page_not_found(e):
    return u"页面不见了 %s" % e

if __name__ == '__main__':
    app.run(debug=True)

