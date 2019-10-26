import math


class Circle:
    '''
    分别使用property的两种使用方法， 实现 面积s 和 半径r 的操作
    '''

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return round(self.radius, 1)

    def set_radius(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError('wronge type')
        self.radius = radius

    # property用法一
    # @property  和  @函数名.setter装饰器
    @property
    def S(self):
        return self.radius ** 2 * math.pi

    @S.setter
    def S(self, s):
        self.radius = math.sqrt(s / math.pi)

    # property 用法二
    # 参数分别是  属性的访问 属性的赋值  属性的删除   都是函数参数
    R = property(get_radius, set_radius)


c = Circle(5.712)

c.S = 99.88
print(c.S)  # 99.880000000
print(c.R)  # 5.6
print(c.get_radius())  # 5.6