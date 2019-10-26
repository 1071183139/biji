from multiprocessing import Process, Queue
import time

def get_num(queue):
    time.sleep(1)
    res = queue.get()
    print('获取了', res)

def put_num(queue):
    print("放入了", 1)
    queue.put(1)

if __name__ == "__main__":
    """
    po.close() #关闭进程池，关闭后po不再接收新的请求
    po.join() #等待po中所有子进程执行完成，必须放在close语句之后
    """
    #使用消息队列
    queue = Queue()
    task1 = Process(target=put_num, args=(queue,))
    task2 = Process(target=get_num, args=(queue,))
    task1.start()
    task2.start()
