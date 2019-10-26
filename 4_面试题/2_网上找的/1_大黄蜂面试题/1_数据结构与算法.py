from collections import Counter,namedtuple,deque
from collections import OrderedDict,defaultdict



# Counter 统计每个字母出现的次数
a='abcdsscaaa'
s=Counter(a)
# print(s)  #Counter({'a': 4, 's': 2, 'c': 2, 'd': 1, 'b': 1})

#值大到小的一个数量
# print(s.most_common())  #[('a', 4), ('c', 2), ('s', 2), ('b', 1), ('d', 1)]



#deque 双端队列
de=deque()
de.append(0)
de.appendleft(2)
# print(de)  #deque([2, 0])

a=de.pop()
# print(a)  #0

b=de.popleft()
# print(b) #2


# OrderedDict 字典赋值的顺序(k的顺序)
po=OrderedDict()
po['c']='c'
po['b']='b'
po['a']='a'
# print(po)  #OrderedDict([('c', 'c'), ('b', 'b'), ('a', 'a')])


# defaultdict 带有默认值的字典
dd=defaultdict(int)
print(dd['a'])  #0
dd['b']+=1
print(dd)  #defaultdict(<class 'int'>, {'a': 0, 'b': 1})
