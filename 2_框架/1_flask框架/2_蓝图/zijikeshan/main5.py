#coding:utf8

from flask import Flask
from Cart import cart_app

app=Flask(__name__)
app.register_blueprint(cart_app,url_prefix='/cart')

if __name__ == '__main__':
    app.run(debug=True)

