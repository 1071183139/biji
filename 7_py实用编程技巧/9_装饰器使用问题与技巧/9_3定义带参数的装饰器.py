import inspect


def type_assert(*ty_args, **ty_kwargs):  # 带参数的装饰器函数， 要增加一层包裹    参数是 装饰器的参数
    def decorator(func):
        # inspect.signature(func)  函数观察对象， 方便后面获取 参数-类型 字典与参数-值字典
        func_sig = inspect.signature(func)  # (a,b,c)
        # 将装饰器参数  组成参数-类型 字典  如  {a:int, b:str}
        bind_type = func_sig.bind_partial(*ty_args, **ty_kwargs).arguments  # OrderedDict([('c', <class 'str'>)])

        # func_sig.bind_partial      绑定部分参数可以得到 参数类型字典，
        # 比如 参数是a=1, b='bbbb', c=2    装饰器参数是 a=int, b=str   ,则得到{'a':int, 'b':str}
        # 如果使用 func_sig.bind    则装饰器参数中   不能缺少  c 的类型
        def wrap(*args, **kwargs):  # 参数是func的 参数
            for name, obj in func_sig.bind(*args, **kwargs).arguments.items():  # 得到 参数-值 字典
                type_ = bind_type.get(name)  # 从 参数-类型  字典中  得到 参数 应该属于的 类型
                if type_:
                    if not isinstance(obj, type_):
                        raise TypeError('%s must be %s' % (name, type_))
            return func(*args, **kwargs)

        return wrap

    return decorator


@type_assert(c=str)
def f(a, b, c):
    pass


if __name__ == '__main__':
    f(5, 10, 's')  # 校验通过
    # f(5, 10, 1)  # 检验失败 1 不是字符串类型