
from multiprocessing import Process
import time
import os

def func(e):
    print(e)
    time.sleep(e)

if __name__=="__main__":
    task1=Process(target=func, args=(1,))
    task2=Process(target=func, args=(2,))
    task1.start()
    task2.start()


