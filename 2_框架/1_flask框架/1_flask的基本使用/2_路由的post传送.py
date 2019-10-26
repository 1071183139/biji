# coding:utf8

from flask import Flask


# 创建一个应用对象
app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    return "hello word"


if __name__ == '__main__':
    app.run()