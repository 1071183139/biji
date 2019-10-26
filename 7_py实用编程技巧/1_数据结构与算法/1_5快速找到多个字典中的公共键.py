from random import randint,sample
# 取样
# print(sample('abcdef',3)) # 随机去 3 个




# 方案一： 利用集合的交集操作
# from random import randint,sample
# # 取样
# s1 = {x:randint(1,4) for x in sample('abcdef',randint(3,6))}
# s2 = {x:randint(1,4) for x in sample('abcdef',randint(3,6))}
# s3 = {x:randint(1,4) for x in sample('abcdef',randint(3,6))}
# print(s1)
# print(s2)
# print(s3)
# print(s3.keys())
# print('resuit ===========')
# print(s1.keys() & s2.keys() & s3.keys())







from random import randint, sample
from functools import reduce

s1 = {x: randint(1, 4) for x in sample('abcdef', randint(3, 6))}
s2 = {x: randint(1, 4) for x in sample('abcdef', randint(3, 6))}
s3 = {x: randint(1, 4) for x in sample('abcdef', randint(3, 6))}
dl = [s1, s2, s3]
print(s1)
print(s2)
print(s3)
print('result======')
print(list(map(dict.keys,dl)))
print(reduce(lambda a, b: a & b, map(dict.keys, dl)))



# step1 使用字典的keys方法， 得到一个字典keys的集合
# step2 使用map函数， 得到每个字典keys的集合
# step3 使用reduce函数， 取所有字典的keys集合的交集

