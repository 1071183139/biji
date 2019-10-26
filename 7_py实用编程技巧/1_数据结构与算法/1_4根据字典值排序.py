# 元祖进行比较，先比较第一个元素，在比较第二个元素
# print((97, 'a') > (96, 'b'))
# print((97, 'a') > (97, 'b'))


# 利用zip将字典转换成元组进行排序
# from random import randint
# d = {x:randint(60,100) for x in 'xyzabc'}
# print(d)
# print(list(zip(d.values(),d.keys())))
# print(sorted(zip(d.values(),d.keys())))


from random import randint
d = {x:randint(60,100) for x in 'xyzabc'}
print(sorted(d.items(),key=lambda x:x[1]))