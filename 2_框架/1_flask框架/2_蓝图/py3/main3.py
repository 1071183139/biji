# -*- coding:utf-8 -*-
from flask import Flask, request
from cart import cart_app

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

# 注册蓝图：将 user_app这个蓝图中所有的路由添加到app的url_map中
app.register_blueprint(cart_app, url_prefix='/cart')

if __name__ == '__main__':
    print app.url_map
    app.run(debug=True)