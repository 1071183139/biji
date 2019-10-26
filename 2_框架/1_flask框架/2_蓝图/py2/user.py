# -*- coding:utf-8 -*-


from flask import Blueprint

# 创建蓝图对象，指定两参数：蓝图的名字，导入的模块名
user_app = Blueprint('user', __name__)

#在这个蓝图对象上进行操作,注册路由,指定静态文件夹,注册模版过滤器
@user_app.route('/user_info')
def user_info():
    return "user_info"