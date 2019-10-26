# class Data(object):
#     def __init__(self, value, node):  # 定义数据的值，和属于的结点
#         self.node = node
#         self.value = value
#
#     def __str__(self):
#         return "%s 's data,value is %s" % (self.node, self.value)
#
#     def __del__(self):
#         print('in Data.__del__')
#
#
# class Node(object):
#     def __init__(self, value):  # 定义一个结点，并赋初值数据。
#         self.data = Data(value, self)  # 结点的数据是Data（）类的对象，
#
#     def __del__(self):
#         print('in Node.__del__')
#
#
# node = Node(100)
#
# del node
# print('end')






# 先输出的是 end 说明循环引用没有被释放　　
#
# 使用 弱引用进行改写
import weakref


class Data(object):
    def __init__(self, value, node):
        self.node = weakref.ref(node)  # 创建结果的弱引用对象
        self.value = value

    def __str__(self):
        return "%s 's data,value is %s" % (self.node(), self.value)

    def __del__(self):
        print('in Data.__del__')


class Node(object):
    def __init__(self, value):
        self.data = Data(value, self)

    def __del__(self):
        print('in Node.__del__')


node = Node(100)

del node
print('end')