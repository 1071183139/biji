from celery_app import app
import time


@app.task
def multiply(x,y):
    print('enter call func......')
    time.sleep(4)
    return x*y