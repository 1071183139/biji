# -*- coding:utf-8 -*-


from flask import Flask, make_response, session,g

app = Flask(__name__)
app.secret_key = "aaa"

def login_required(f):
    def wrapper(*args, **kwargs):
        g.user_id = "18"
        return f(*args, **kwargs)

    return wrapper

@app.route('/')
@login_required
def index():
    user_id = g.user_id
    return user_id

if __name__ == '__main__':
    app.run(debug=True)