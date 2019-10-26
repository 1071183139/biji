# -*- coding:utf-8 -*-


from flask import Flask, abort

app = Flask(__name__)


@app.route('/')
def index():
    print "要返回内容了"
    return 'index'


# 第一次请求之前，只会执行一次，可以在此函数中做一些请求前的初始化操作
@app.before_first_request
def before_first_request():
    print "第1次请求之前"


@app.before_request
def before_request():
    print "请求之前"

    # 如果直接在这个函数里面返回数据的话，那么真实的视图函数就不会被执行了
    # 可以在此函数中做一些请求的判断
    # return u"哈哈"

# 如果没有未处理的异常抛出，在每次请求后运行。
@app.after_request
def after_request(response):
    print "请求之后"
    return response


# 请求销毁的时候执行，一定会执行，不管服务器有没有抛出错误 ，一定会执行
@app.teardown_request
def teardown_request(error):
    print "请求销毁之后"

if __name__ == '__main__':
    print app.url_map
    app.run(debug=True)