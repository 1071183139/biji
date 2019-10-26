import threading
from threading import Lock
total = 0
lock = Lock()

def add():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()  # 获取锁
        total += 1
        lock.release() # 释放锁

def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()  # 获取锁
        total -= 1
        lock.release()  # 释放锁

if __name__ == '__main__':
    thread1 = threading.Thread(target=add)
    thread2 = threading.Thread(target=desc)
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print(total)
