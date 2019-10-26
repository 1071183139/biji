from threading import Event,Thread
import time
def f(e):
    print('f 0')
    e.wait()      #事件等待，阻塞
    print('f 1')
if __name__ == '__main__':
    e = Event()
    t = Thread(target=f, args=(e,))  #创建子线程，运行f函数
    t.start()  # 子线程运行
    time.sleep(5)
    e.set()  # 主线程里 事件发送

# 等待事件一端调用wait, 等待事件
# 通知事件一端调用 set， 通知事件