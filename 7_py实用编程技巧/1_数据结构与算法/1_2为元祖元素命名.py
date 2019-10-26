# 定义一系列数值常量或枚举类型

student = ('Jim', 16, 'male', 'jim8721@gmail.com')

#第一种方法
# NAME, AGE, SEX, EMAIL = range(4)
# print(student[NAME])
# print(student[AGE])
# print(student[SEX])
# print(student[EMAIL])


#第二种方法
# 使用 python3 中的枚举类型
from enum import IntEnum

class StudentEnum(IntEnum):
    NAME = 0
    AGE = 1
    SEX = 2
    EMAIL = 3

# print(student[StudentEnum.NAME])
# print(student[StudentEnum.AGE])
# print(student[StudentEnum.SEX])
# print(student[StudentEnum.EMAIL])

#第三种方法
# 使用标准库中 collections.namedtuple 替代内置tuple
from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])

s2 = Student('Jim', 16, 'male', 'jim8721@gmail.com')

print(s2.name)
print(s2.age)
print(s2.sex)
print(s2.email)


