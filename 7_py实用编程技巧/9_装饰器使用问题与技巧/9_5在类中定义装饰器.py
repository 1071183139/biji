import time
import logging

DEFAULT_FORMAT = '%(func_name)s -> %(call_time)s\t%(used_time)s\t%(call_n)s'


class CallInfo:
    def __init__(self, log_path, format_=DEFAULT_FORMAT, on_off=True):
        self.log = logging.getLogger(log_path)
        self.log.addHandler(logging.FileHandler(log_path))
        # 这样可以通过log 往  log_path 输出信息
        self.log.setLevel(logging.INFO)  # 设置log级别
        self.format = format_
        self.is_on = on_off

    # 装饰器方法
    def info(self, func):
        _call_n = 0  # 被调用次数

        def wrap(*args, **kwargs):
            func_name = func.__name__
            call_time = time.strftime('%x %X', time.localtime())
            # localtime 格式化时间戳为本地的时间    strftime 则得到时间字符串
            # % x
            # 本地相应的日期表示
            # % X
            # 本地相应的时间表示
            t0 = time.time()
            res = func(*args, **kwargs)
            used_time = time.time() - t0
            nonlocal _call_n
            _call_n += 1
            call_n = _call_n
            if self.is_on:
                self.log.info(self.format % locals())  # locals  即wrap函数中的变量 对应的字典
            return res

        return wrap

    def set_format(self, format_):
        self.format = format_

    def turn_on_off(self, on_off):
        self.is_on = on_off


# 测试代码
import random

ci1 = CallInfo('mylog1.log')
ci2 = CallInfo('mylog2.log')


@ci1.info
def f():
    sleep_time = random.randint(0, 6) * 0.1
    time.sleep(sleep_time)


@ci1.info
def g():
    sleep_time = random.randint(0, 8) * 0.1
    time.sleep(sleep_time)


@ci2.info
def h():
    sleep_time = random.randint(0, 7) * 0.1
    time.sleep(sleep_time)


for _ in range(3):
    random.choice([f, g, h])()

ci1.set_format('%(func_name)s -> %(call_time)s\t%(call_n)s')  # 去掉使用时间
for _ in range(3):
    random.choice([f, g])()
