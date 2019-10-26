# -*- coding:utf-8 -*-
# 放置的是Cart模块的所的视图函数

from flask import render_template
from . import bart_app


@bart_app.route('/bart_page')
def bart_page():
    return render_template('bart.html')