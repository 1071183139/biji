# import sys
#
#
# class A(object):
#     def __del__(self):  # 析构函数，在垃圾回收器回收变量时会调用析构函数
#         print('in __del__')
#
#
# if __name__ == '__main__':
#     a = A()
#     print(sys.getrefcount(a))  # 打印a的循环引用计数
#     a1 = a
#     print(sys.getrefcount(a))  # 打印a的循环引用计数
#     del a1
#     print(sys.getrefcount(a))  # 打印a的循环引用计数
#     a = 5  # 将a赋值 时，a的引用计数再减1，就不再使用了，此时垃圾回收器将回收这个变量





import sys
import weakref


class A(object):
    def __del__(self):  # 析构函数，在垃圾回收器回收变量时会调用析构函数
        print('in __del__')


if __name__ == '__main__':
    a = A()
    print(sys.getrefcount(a))  # 打印 a 的循环引用计数
    # 创建a的弱引用对象
    a_wref = weakref.ref(a)
    print(sys.getrefcount(a))  # 此时a的循环引用计数，数量不变
    a2 = a_wref()  # 将弱引用对象赋给a2
    print(sys.getrefcount(a))  # 此时的引用计数增加了
    print(a2 is a)
    print(sys.getrefcount(a2))  # 查看a2的循环引用计数

    # 删除a和a2
    del a2
    del a

    print(a_wref() is None)  # 此时弱引用对象已回收，返回None





