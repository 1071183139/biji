# coding:utf8
from flask import Flask

app = Flask(__name__)


@app.route("/num/<int:id>")
def demo1(id):
    return u"接受到的参数是%s" % id


if __name__ == '__main__':
    app.run(debug=True)