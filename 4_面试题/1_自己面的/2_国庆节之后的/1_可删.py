dict={'name':'zyc','age':18}
# del dict['name']
# dict.pop('age')
# print(dict)


list=[1,2,3,4,5]
a=set(list)
# print(a)
# print([x for x in a])


# def func(a,b,*args,**kwargs):
#     res=a*b
#     print(*args)
#     for k,v in kwargs.items():
#         print(k,v)
#
#     return res
# s=func(2,3,5,7,9,name='zyc')
# print(s)

# print(type(range(100)))



# class danli():
#     def __init__(self,name):
#         self.name=name
#
#     __isinstance = False
#     def __new__(cls, *args, **kwargs):
#
#         if cls.__isinstance==False:
#             cls.__isinstance=object.__new__(cls)
#         return cls.__isinstance



# a=danli('小狗')
# print(id(a))
# b=danli('小猫')
# print(id(b))



# with open('./a.txt','r+') as f:
#     # f.write('12345678')
#     s=f.read()
#     print(s)


import random
import random as np
# a=random.randint(1,10)
# print(a)
#
# b=random.random()
# print(b*100)

# a=1000
# b=1000
# print(id(a))
# print(id(b))

# a=(1,2,3)
# a+=(4,5)
# b=a+(7,8)
# print(a)
# print(b)


# a=[1,2,3,4]
# print(id(a)) #140619609109128
# a.remove(1)
# print(id(a)) #140619609109128
#
#
# a=[1,2,3]
# print(id(a)) #140619609087688
#
# a=[1,2,4]
# print(id(a)) #140619609109128

# s = "ajldjlajfdljfddd"
# s=set(s)
# print(s)
# a=sorted(s,reverse=False)
# print(a)
# s1=''.join(a)
# print(s1)


# s="kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
# from collections import Counter
# s1=s.split(';')
# print(s1)
# a=Counter(s1)
# print(a)

#列表，元祖，字符串
# a='1234'
# b='5678'
# s=zip(a,b)
# s1=[x for x in s]
# print(s1)

# s='晓莫名 98分'
# import re
# res=re.sub(r'\d+','100',s)
# print(res)


# a=[1,2,3]
# b=[4,5]
# a.extend(b)
# print(a)




# a=[2,3,5,4,9,6]
# list=[]
# def func(a):
#     n=min(a)
#     list.append(n)
#     a.remove(n)
#     if len(a)>0:
#         func(a)
#     return list
# res=func(a)
# print(res)

# a=1.1111111
# print("%.02f"%a)
# print("%d"%a)

del dict
# dict0 = dict()  # 传一个空字典
# print('dict0:', dict0)


# dict1 = dict({'three': 3, 'four': 4})  # 传一个字典
# print('dict1:', dict1)
# #
# dict2 = dict(five=5, six=6)  # 传关键字
# print('dict2:', dict2)
# #
# dict3 = dict([('seven', 7), ('eight', 8)])  # 传一个包含一个或多个元祖的列表
# print('dict3:', dict3)
# #
# dict5 = dict(zip(['eleven', 'twelve'], [11, 12]))  # 传一个zip()函数
# print('dict5:', dict5)
#
# dict6=dict([('name','age'),('zu',18)])
# print('dict6',dict6)

# a=' 2222  '
# print(a)
# a1=a.strip()
# print(a1)

# foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
# res=sorted(foo,key=lambda x:(x<0,abs(x)))
# print(res)


#
# dic={'name':'zyc','age':18,'city':'shanghai'}
# res=sorted(dic.items(),key=lambda x:x[0])
# print(res)
# dic2={i[0]:i[1] for i in res}
# print(dic2)

# str=" hello world shijie nihao "
# # res=str.replace(' ','')
# # print(res)
# list=str.split(' ')
# print(list)
# res=''.join(list)
# print(res)


import random
# res=random.choice(range(1,101))
# print(res)


import re


# match
# 匹配string 开头，成功返回Match object, 失败返回None，只匹配一个。
# search
# 在string中进行搜索，成功返回Match object, 失败返回None, 只匹配一个。
# findall
# 在string中查找所有 匹配成功的组, 即用括号括起来的部分。返回list对象，每个list item是由每个匹配的所有组组成的list。
s="小明年龄18 工资10000"
res=re.search(r'\d+',s).group()
print("search返回的结果:",res)

res=re.findall(r'\d+',s)
print("findall返回的结果:",res)

res=re.match("小明",s).group()
print("1match返回的结果:",res)

# match不加group是不对的。
res=re.match(r'\d+',s)
print("试错，match返回的结果:",res)

#没有工资开头的所以报错
res=re.match("工资",s).group()
print("2match返回的结果:",res)








