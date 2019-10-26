import time
# def fibonacci(n):
#     if n<=1:
#         return 1
#     return fibonacci(n-1)+fibonacci(n-2)
#
# s=time.time()
# res=fibonacci(20)
# e=time.time()
# print(e-s)
# print(res)


def fibonacci(n,cache=None):
    #cache(n)  #计算开始时先去缓存里找是否计算过n，如存在直接返回，否则计算，并把计算结果放在缓存中。
    if cache is None:  #创建一个空的字典
        cache = {}
    if n in cache:
        return cache[n]
    if n<=1:
        return 1
    cache[n] = fibonacci(n-1,cache) + fibonacci(n-2,cache)
    return cache[n]
if __name__ == '__main__':
    e=time.time()
    print(fibonacci(50))
    s=time.time()
    print(s-e)


def memo(func):
    cache = {}

    def wrap(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    return wrap


@memo
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    e = time.time()
    print(fibonacci(50))
    s = time.time()
    print(s - e)