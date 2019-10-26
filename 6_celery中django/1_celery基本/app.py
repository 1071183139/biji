import time
from tasks import add

if __name__ == '__main__':
    print('start task')
    result = add.delay(2, 3)
    print(result)