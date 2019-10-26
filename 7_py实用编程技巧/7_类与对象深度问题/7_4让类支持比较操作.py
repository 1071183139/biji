from functools import total_ordering

from abc import ABCMeta, abstractclassmethod


@total_ordering  # 修饰后， 只要实现__eq__ 和 剩下的比较操作中 随便实现一个， 就能实现所有比较
class Shape(metaclass=ABCMeta):  # 定义抽象类
    @abstractclassmethod  # 定义抽象方法
    def area(self):
        pass

    def __lt__(self, obj):
        print('__lt__', self, obj)
        return self.area() < obj.area()

    def __eq__(self, obj):
        return self.area() == obj.area()


class Rect(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def __str__(self):
        return 'Rect:(%s, %s)' % (self.w, self.h)


import math


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r ** 2 * math.pi


rect1 = Rect(6, 9)  # 54
rect2 = Rect(7, 8)  # 56
c = Circle(8)  # 201.06

print(rect1 < c)  # True
print(c > rect2)  # True