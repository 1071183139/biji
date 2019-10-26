#coding:utf8
from flask import Flask,json

app = Flask(__name__)

# json.dumps 返回的不是真的json格式
# 前端显示Content-Type:text/html; charset=utf-8

@app.route("/")
def do_json():
    strs = {"name":"zhang"}
    return json.dumps(strs)

if __name__ == '__main__':
    app.run(debug=True)