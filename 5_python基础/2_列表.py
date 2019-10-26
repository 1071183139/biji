namesList = ['xiaoWang','xiaoZhang','xiaoHua']

length = len(namesList)
def func():
    i = 0

    while i<length:
        print(namesList[i])
        i+=1
# func()


# 列表的增加(append 末尾增加，insert 插入，extend 扩展)
li1=['nihao','1','zhang','hello','1','world','1']
# li1.append('zhangbiao')
# print(li1)

# li1.insert(1,2)
# print(li1)

li2=[1,2,3,4,5]
li2.extend(li1)
# print(li2)

#修改元素，主要是通过下标确定
# li1[4]='zhangdada'
# print(li1)

# 查找元素(in,not in,index,count)
# in 存在 not in 不存在（用法一样，意义相反）
# find_name=input('请输入要找的名字：')
# if find_name in li1:
#     print('找到了')
# else:
#     print('没有找到')

# index 返回第一次的索引
# print(li1.index('1',5,len(li1)))

# count 计算str出现的次数 count 只能接受一个参数。
# print(li1.count('1'))

# 删除元素（pop,remove,del）
# del：根据下标进行删除
# print(li1)
# del li1[0]
# print(li1)
# pop：删除最后一个元素
# print(li1.pop())
# print(li1)
# remove：根据元素的值进行删除
li1.remove('zhang')
# print(li1)

# 列表的排序 sort reverse
li=[1,3,5,2,4]
# li.sort() # 不写默认由小到大
# li.sort(reverse=True) # 参数reverse=True可改为倒序，由大到小
li.reverse() # reverse 将li逆序
print(li)

#元组（不能被修改# ）
# index和count与字符串和列表中的用法相同