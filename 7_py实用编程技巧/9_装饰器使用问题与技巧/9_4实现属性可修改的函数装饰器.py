import time
import logging


def warn_timeout(timeout):
    def decorator(func):
        # _timeout = [timeout]
        def wrap(*args, **kwargs):
            # timeout = _timeout[0]
            t0 = time.time()
            res = func(*args, **kwargs)
            used = time.time() - t0
            if used > timeout:
                logging.warning('%s: %s > %s', func.__name__, used, timeout)  # logging.warning 打印 输出到控制台
            return res

        def set_timeout(new_timeout):
            nonlocal timeout  # timeout 是闭包 变量
            timeout = new_timeout
            # _timeout[0] = new_timeout

        wrap.set_timeout = set_timeout  # 使timeout 可修改
        return wrap

    return decorator


import random


@warn_timeout(1.5)
def f(i):
    print('in f [%s]' % i)
    while random.randint(0, 1):
        time.sleep(0.6)


for i in range(3):
    f(i)

f.set_timeout(1)  # 修改timeout  参数    从1.5 变为1
for i in range(3):
    f(i)