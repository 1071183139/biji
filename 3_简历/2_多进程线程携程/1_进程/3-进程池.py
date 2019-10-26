from multiprocessing import Pool

def func(url):
    print(url)

li = ['url1','url2','url3']

if __name__=="__main__":
    """
    po.close() #关闭进程池，关闭后po不再接收新的请求
    po.join() #等待po中所有子进程执行完成，必须放在close语句之后
    """
    po = Pool(3)

    for url in li:
        po.apply_async(func, args=(url,))

    po.close()
    po.join()