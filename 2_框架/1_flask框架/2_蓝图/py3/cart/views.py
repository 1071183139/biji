# -*- coding:utf-8 -*-
# 放置的是Cart模块的所的视图函数

from flask import render_template
from . import cart_app

@cart_app.route('/cart_list')
def cart_list():
    return 'cart_list'