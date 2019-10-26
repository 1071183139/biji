import time
from celery import Celery

# 消息中间件
broker = 'redis://localhost:6379/1'

# 存取任务执行的结果
backend = 'redis://localhost:6379/2'

app = Celery('my_task', broker=broker, backend=backend)


@app.task
def add(x, y):
    print('enter call func......')
    time.sleep(4)
    return x + y