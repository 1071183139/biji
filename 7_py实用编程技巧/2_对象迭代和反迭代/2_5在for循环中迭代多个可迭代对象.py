# from random import randint
#
# chinese = [randint(60, 100) for _ in range(10)]
# print(chinese)
# math = [randint(60, 100) for _ in range(10)]
# english = [randint(60, 100) for _ in range(10)]
#
# total = []
# for c, m, e in zip(chinese, math, english):
#     total.append(c + m + e)
#
# print(total)



from random import randint
from itertools import chain

c1 = [randint(60, 100) for _ in range(40)]
c2 = [randint(60, 100) for _ in range(41)]
c3 = [randint(60, 100) for _ in range(42)]
c4 = [randint(60, 100) for _ in range(43)]

count = 0

for s in chain(c1, c2, c3, c4):
    if s > 90:
        count += 1
print(count)






