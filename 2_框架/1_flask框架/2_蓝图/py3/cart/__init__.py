# -*- coding:utf-8 -*-

from flask import Blueprint

# 创建蓝图对象，指定两参数：蓝图的名字，导入的模块名
cart_app=Blueprint('cart',__name__)

#为了执行views里的函数
from views import cart_list