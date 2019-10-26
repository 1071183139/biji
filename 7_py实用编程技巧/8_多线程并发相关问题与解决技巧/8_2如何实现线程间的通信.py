from threading import Thread
from queue import Queue
from time import sleep


class DownThread(Thread):
    def __init__(self, sid, queue):
        # Thread.__init__(self)
        super(DownThread, self).__init__()
        self.sid = sid
        self.queue = queue

    def downLoad(self, sid):
        print("Download (%d)..." % sid)
        sleep(2)

    def run(self):
        self.downLoad(self.sid)
        data = self.sid + 100
        self.queue.put((self.sid, data))


class ConvelThread(Thread):
    def __init__(self, queue):
        # Thread.__init__(self)
        super(ConvelThread, self).__init__()
        self.queue = queue

    def convel(self, id, data):
        print("Convel  (%d)-(%d)" % (id, data))

    def run(self):
        while (True):
            id, data = self.queue.get()  # 元组解包的形式得到数据
            if (data):
                self.convel(id, data)


if __name__ == '__main__':
    q = Queue()
    dThreads = [DownThread(i, q) for i in range(1, 11)]
    cThread = ConvelThread(q)
    for t in dThreads:
        t.start()

    cThread.start()
    for t in dThreads:
        t.join()
    q.put((-1, None))  # 往队列中写入-1使 转换线程结束
    cThread.join()
    print('MainThread')
