from random import randint
from collections import deque

N = randint(0, 100)
history = deque([], 5)


def guess(k):
    if k == N:
        print('Right')
        return True
    if k < N:
        print('%s is less-than N' % k)
    else:
        print('%s is greater-than N' % k)
    return False


while True:
    line = input('Please input a number:')
    if line.isdigit():
        k = int(line)
        history.append(k)
        if guess(k):
            break
    elif line == 'history' or line == 'h':
        print(list(history))





# plckle 基本使用
# from collections import deque
# import pickle
#
# q = deque([2, 3, 4, 5, 6])
# print(q)
#
# # 将数据存入文件
# pickle.dump(q, open('history', 'wb'))
# # 读取文件
# q2 = pickle.load(open('history', 'rb'))
# print(q2)
