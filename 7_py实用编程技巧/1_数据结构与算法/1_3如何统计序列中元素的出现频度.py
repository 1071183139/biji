# 将序列转化为字典{元素: 频度}， 根据字典中的值排序　
from random import randint

data = [randint(0, 20) for _ in range(30)]
# print('date:',data)

# fromkeys：用于创建并返回一个新的字典。两个参数：第一个是字典的键，第二个（可选）是传入键的值，默认为None。
c = dict.fromkeys(data, 0)
# print('c:',c)

for x in data:
    c[x] += 1
# print('c:',c)
# 如果只是想取出最大的3个，可以使用堆代替排序后再取值的方法

import heapq

res2 = heapq.nlargest(3, ((v, k) for k, v in c.items()))
# print('res2:',res2)











from collections import Counter
from random import randint

data = [randint(0, 20) for _ in range(30)]
c2 = Counter(data)
# print(c2)
# 找出频率出现最高的３个元素
# print(c2.most_common(3))









#实际使用
from collections import Counter
import re

txt = open('example.txt').read()  # 读入文件
wordList = re.split('\W+', txt)
c2 = Counter(wordList)  # 可以传入列表或者字典
res4 = c2.most_common(10)
print(res4)