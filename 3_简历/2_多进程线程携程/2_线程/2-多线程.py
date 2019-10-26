
from threading import Thread
import time
import os


def func(url):
    print(url)

li = ['url1','url2','url3']

if __name__=="__main__":

    for url in li:
        t = Thread(target=func,args=(url,))
        t.start()


