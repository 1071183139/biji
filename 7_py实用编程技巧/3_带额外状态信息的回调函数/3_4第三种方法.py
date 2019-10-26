# 异步回调
def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))


def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)
    return 'ok'


def add(x, y):
    return x + y


if __name__ == '__main__':
    handler = make_handler()
    next(handler)
    res = apply_async(add, (2, 3), callback=handler.send)
    res = apply_async(add, ('hello', 'world'), callback=handler.send)