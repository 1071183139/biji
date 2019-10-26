# coding:utf8
from flask import Flask

app = Flask(__name__)


@app.route("/user/<user_id>")
def demo(user_id):
    # return u"接受的参数是 %s" % user_id
    return user_id


if __name__ == '__main__':
    app.run(debug=True)