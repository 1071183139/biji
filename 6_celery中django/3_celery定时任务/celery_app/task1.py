from celery_app import app
import time


@app.task
def add(x,y):
    print('enter call func......')
    time.sleep(4)
    return x+y