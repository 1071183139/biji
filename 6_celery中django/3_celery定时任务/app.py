from celery_app.task1 import add
from celery_app.task2 import multiply




if __name__ == '__main__':
    print('start task')
    result1 = add.delay(2,3)
    result2 = multiply.delay(4,5)
    print('end')