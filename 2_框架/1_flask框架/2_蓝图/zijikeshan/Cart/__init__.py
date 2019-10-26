#coding:utf8
from flask import Flask,Blueprint

#创建一个蓝图对象
cart_app = Blueprint('user',__name__)

#为了执行views里的函数
from views import index
