class Player1:
    def __init__(self, uid, name, level):
        self.uid = uid
        self.name = name
        self.level = level


class Player2:
    __slots__ = ['uid', 'name', 'level']

    def __init__(self, uid, name, level):
        self.uid = uid
        self.name = name
        self.level = level


p1 = Player1('0001', 'Jim', '20')
p2 = Player2('0001', 'Jim', '20')

print(set(dir(p1)) - set(dir(p2)))
# 发现p1属性 多于p2
# 多了  __dict__,  和__weakref__两个属性
# 主要在__dict__  属性上 会多消耗内存
# __dict__ 动态维护 实例属性  像self.uid  self.name  这些都是它维护的,
# __dict__ 可以动态添加属性  如  p1.newadd = 1   会自动在p1.__dict__的字典中加入 'newadd': 1

import sys

print(sys.getsizeof(p1.__dict__))  # 864
print(sys.getsizeof(p1.name))  # 52
print(sys.getsizeof(p1.level))  # 28
print(sys.getsizeof(p1.uid))  # 53
# 可以看到 __dict__浪费了一部分内存， 如果实例比较少， 问题不大， 但实例非常多， 会非常浪费内存

# 如果使用了__slots__   就提前确定的内存， 无法对实例动态添加属性了  像 p2.newadd = 1 就会报错，无法实现。
# 原有属性不受影响   p2.name = "newname"  都是可行的