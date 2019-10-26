from time import time
from random import randint
from collections import OrderedDict

d = OrderedDict()
players = list('ABCDEFGH')
start = time()

for i in range(8):
    '''模拟选手比赛消耗时间并存入字典中'''
    input()
    p = players.pop(randint(0, 7 - i))
    end = time()
    print(i + 1, p, end - start, sep=' ')
    d[p] = (i + 1, end - start)

print('-' * 30)

for k in d:
    print(k, d[k])