# -*- coding:utf-8 -*-
from flask import Flask, request
from user import user_app

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

# 注册蓝图：将 user_app这个蓝图中所有的路由添加到app的url_map中
app.register_blueprint(user_app, url_prefix='/user')

if __name__ == '__main__':
    print app.url_map
    app.run(debug=True)

# 蓝图的总结：在其他的模块中，用蓝图来管理这个模块中的所有路由。再把蓝图传给最主要的模块里，注册下蓝图。