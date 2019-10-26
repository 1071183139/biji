from threading import Thread
from time import sleep


def handle(sid):
    print('Download...(%d)' % sid)
    sleep(2)
    print('Convert to...(%d)' % sid)


class MyThread(Thread):  # 自定义线程类
    def __init__(self, sid):
        # Thread.__init__(self)
        # super(MyThread, self).__init__()  # 必须调用 父类的构造器  这是py2的语法，py3是super().__init__()
        super().__init__()
        self.sid = sid  # 使用类，能够更好的封装数据

    def run(self):  # 新建程序的入口点，和target类似
        handle(self.sid)  # 更常见的做法是将handle也做为这个类的方法


if __name__ == '__main__':
    t = MyThread(1)
    t.start()
    t.join()
    print('main thread')