#coding:utf8
from flask import Flask,jsonify

app = Flask(__name__)

# 前端显示 Content-Type:application/json

@app.route("/")
def do_json():
    strs = {"name": "zhang"}
    return jsonify(strs)


if __name__ == '__main__':
    app.run(debug=True)