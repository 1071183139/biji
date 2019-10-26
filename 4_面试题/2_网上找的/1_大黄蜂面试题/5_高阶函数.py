# map(f,list)是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，
# # 并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的可迭代对象并返回。
# li=[1,2,3,4,5]
# def func(x):
#     return x * x
# li1=map(func,li)
#
# li2=map(lambda x:x*x,li)
#
#
# print(list(li1))
# print([i for i in li2])



# filter方法求出列表所有奇数并构造新列表a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]？
# a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# res=filter(lambda i:i%2==1,a)
# print([i for i in res])


from functools import reduce

def add(x, y) :            # 两数相加
     return x + y

res=reduce(add, [1,2,3,4,5])   # 计算列表和：1+2+3+4+5
print(res)