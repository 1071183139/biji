# 异步回调
class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))


def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)
    return 'ok'


def add(x, y):
    return x + y


if __name__ == '__main__':
    r = ResultHandler()
    res = apply_async(add, (2, 3), callback=r.handler)
    res = apply_async(add, ('hello', 'world'), callback=r.handler)