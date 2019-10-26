# 过滤列表中的负数
from random import randint
data = [randint(-10,10) for _ in range(10)]
# print(data)
# 使用列表解析方法(+filter函数)
# print(list(filter(lambda x:x>0,data)))


# 找出分数大于90的学生

from random import randint
d = {x:randint(60,100) for x in range(1,21)}
# print(d)
#字典解析法
# print({k:v for k,v in d.items() if v > 90 })


#使用filter函数
res=list(filter(lambda x:x[1]>90,d.items()))

dict={}
for k,v in res:
    dict[k]=v
# print(dict)


# 留下集合中的3的倍数
from random import randint
s = {randint(0,20) for _ in range(20)}
# print(s)
# print(list(filter(lambda x:x%3==0,s)))




