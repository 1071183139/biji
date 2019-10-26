from concurrent.futures import ThreadPoolExecutor


def func(url):
    print(url)

li = ['url1','url2','url3']

if __name__=="__main__":
    po = ThreadPoolExecutor(3)

    for url in li:
        po.submit(func,(url,))

    # po = ThreadPoolExecutor(3)
    # tasks = [ po.submit(func, (url,)) for url in li ]








