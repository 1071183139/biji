
from threading import Thread
import time
import os

def func1(e):
    print(e)
    time.sleep(e)

def func2(e):
    print(e)
    time.sleep(e)

if __name__=="__main__":
    task1=Thread(target=func1, args=(1,))
    task2=Thread(target=func2, args=(2,))
    task1.start()
    task2.start()


