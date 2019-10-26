# coding:utf8

from flask import Flask

# 创建一个flask应用程序
app = Flask(__name__)

@app.route("/")
def index():
    return "hello"


if __name__ == '__main__':
    # 输出当前应用所有的路由映射
    print (app.url_map)
    # 运行应用程序
    app.run()