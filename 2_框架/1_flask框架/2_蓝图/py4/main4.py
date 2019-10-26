# -*- coding:utf-8 -*-
from flask import Flask, request
from Bart import bart_app

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

# 注册蓝图：将 user_app这个蓝图中所有的路由添加到app的url_map中
app.register_blueprint(bart_app, url_prefix='/bart')

if __name__ == '__main__':
    print app.url_map
    app.run(debug=True)