# 根据键访问值
info = {'name': '班长', 'id': 100, 'sex': 'f', 'address': '地球亚洲中国北京'}
# print(info['name'])
# print(info['names']) # 键不存在会报错

# get 获取 设置默认值 不存在不会报错
# print(info.get('id'))
# print(info.get('ids','没有这个键'))


# 常见的操作 （修改，增减，删除）
# 修改元素
# new_id=input('请输入元素')
# info['id']=new_id
# print(info1)

#  增加元素  第二个例子
# 如果访问的键存在，就是修改值
# info['id']=18
# print(info)
# 如果访问的键不存在，就是增加元素。
# info['id']=18
# print(info)


# 删除元素（del clear）
# del info[]  或者 del info 删除整个字典
# del info['name']
print(info)

# del info['pp'] # 键不存在会报错
# print(info)

# del info #一种是del加空格，另一种是del()
# print(info) # 删除字典后，字典就不存在。

# clear 清除字典 字典还是存在的，只不过是空字典。
# info.clear()
# print(info)  # {}

# 常见的操作2 (len ,keys ,values,items,has_key)
# len 测量字典中，键值对的个数
# print(len(info))



# keys 返回一个包含字典所有KEY的列表
# print(info.keys())

# values 返回一个包含字典中所有值的列表
# print(info.values())

# items 返回一个包含所有（键，值）元祖的列表
# print(info.items()) #[('name', '班长'), ('id', 100), ('sex', 'f'), ('address', '地球亚洲中国北京')]

# in, not in 判断键是否在字典中
# print('name' in info)

# 遍历
for item in info.items():
    print(item)

for key,value in info.items():
    print(key,value)
    # print(type(key,value))


# 带下标的索引
chars = ['a', 'b', 'c', 'd','f']
chars1=('a','c','v','d','h')
# i = 0
# for chr in chars:
#     print("%d %s"%(i, chr))
#     i += 1

# enumerate # 枚举 列表和元祖都可以。
for i,chr in enumerate(chars1):
    print('%d %s'%(i,chr))

a=(1,2,3,4)
b=('a','b','c','d')
c=a+b
print(a+b)
