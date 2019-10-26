# coding:utf8
from . import cart_app



#在这个蓝图对象上进行操作
@cart_app.route('/cart_info')
def index():
    return 'Hello'


