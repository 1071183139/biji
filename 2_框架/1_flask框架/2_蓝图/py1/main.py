#coding:utf8
from flask import Flask, request
from order import orders

app=Flask(__name__)


app.route('/orders')(orders)


if __name__ == '__main__':
    print app.url_map
    app.run(debug=True)

#最原始的是把装饰器当函数调用，在mian函数里调用其他模块中的函数路由
# 但是这样不好的一点就是，order模块里没有显示路由，感觉不是很清楚