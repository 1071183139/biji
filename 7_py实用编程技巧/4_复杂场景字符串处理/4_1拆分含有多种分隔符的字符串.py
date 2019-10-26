# 1.连续使用str.split()，每一次处理一种分隔符号；
s = "ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz"


def mySplit(s, ds):
    res = [s]
    for i in ds:
        t = []
        # 普通方法
        # for x in res:
        #  t.extend(x.split(i))
        # 列表解析
        # [t.extend(y.split(i)) for y in res if y]
        # map高阶函数,map生成可迭代对象
        for z in map(lambda x: x.split(i), res):
            t.extend(z)
        # 以上三个方法都可以解决问题
        res = t
    # 去除空字符串
    return [x for x in res if x]


# print(mySplit(s, ",;|\t"))







# 2.使用正则表达式的re.split()，一次性拆分字符串
import re

s = "ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz"

print(re.split(r'[,;|\t]+', s))