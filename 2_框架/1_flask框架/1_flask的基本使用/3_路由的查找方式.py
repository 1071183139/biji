from flask import Flask

app = Flask(__name__)

@app.route('/index')
def index1():
    return "hello"


@app.route('/index')
def index2():
    return "hi"

if __name__ == '__main__':
    print app.url_map
    app.run(debug=True)