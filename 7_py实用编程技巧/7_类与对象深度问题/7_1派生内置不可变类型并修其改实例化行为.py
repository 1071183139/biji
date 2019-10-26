class IntTuple(tuple):
    def __new__(cls, iterable):
        g = (x for x in iterable if isinstance(x, int) and x > 0)
        return super(IntTuple, cls).__new__(cls, g)


t = IntTuple([1, -1, 'abc', 6, ['x', 'y'], 3])
print(t)


# 我们想要自定义一种新类型的元组， 对于传入的可迭代对象， 我们只保留作其中int类型且值大于0的元素， 例如：
# IntTuple([1, -1, 'abc', 6, ['x', 'y'], 3]) => (1, 6, 3)
# 如何继承 内置 tuple 实现 IntTuple？
# 解决方案
# 重构 __new__ 方法