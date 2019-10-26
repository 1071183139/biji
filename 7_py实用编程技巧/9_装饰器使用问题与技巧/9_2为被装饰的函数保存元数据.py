from functools import wraps


def mydecorator(func):  # 装饰器，本例没增加功能，只做为演示
    @wraps(func)
    def wrapper(*args, **kargs):
        """wrapper function"""
        print('In wrapper')
        func(*args, **kargs)

    # update_wrapper(wrap, func)
    return wrapper


@mydecorator
def example():
    """example function"""
    print('In example')


if __name__ == '__main__':
    example()
    print(example.__name__)