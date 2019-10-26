#　字符串的格式化输出
# username=input('请输入名字')
# print('你的名字为%s'%username)
#字符串的切片
name = 'abcdef'
# print(name[0])
name = 'abcdef'
# print(name[2:]) # 取 下标为2开始到最后的字符
name = 'abcdef'
# print(name[1:-1]) # 取 下标为1开始 到 最后第2个  之间的字符
# print(name[::-1]) # fedcba 逆序  步长为1
# print(name[::-2])  # fdb 逆序 步长为2

# format函数
# str='{1}-{0}'.format('biao','zhang')
# str='{} {}'.format('zhang','yang','cheng')
# str='{name}-{age}'.format(name='yangmi',age=12)
li=[1,2,3,4,5]
str='{0[0]} {0[1]}'.format(li)
# print(str)

# 字符串常见的操作
# find 查找 有，返回下标，没有返回-1
# mystr.find(str, start=0, end=len(mystr))

mystr = 'hello world itcast and itcastcppm'
# print(mystr.find('and'))
# print(mystr.find('and',0,len(mystr)))
# print(mystr.find('and',0,18))

# index 和find一样 没有会报错
# print(mystr.index('m',0,len(mystr)))
# print(mystr.index('m',0,-1))

# count 返回str在start和end之间 在 mystr里面出现的次数
# mystr.count(str, start=0, end=len(mystr))
# print(mystr.count('p'))


# replace 替换 str1替换成str2
mystr2='ha ha ha ha'
# print(mystr2.replace('ha','Ha'))
# print(mystr2.replace('ha','Ha',mystr2.count('ha')))
# print(mystr2.replace('ha','Ha',1))

#split 分割 以str 为分隔符切片mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串
# print(mystr.split(' ',2))
# print(mystr.split(' '))

# startswith endswith 判断字符串以什么开头，以什么结尾
# print(mystr.startswith('world'))
# print(mystr.endswith('itcastcpp'))

#lower upper 将转化为大写，转换为小写
# print(mystr.lower())
# print(mystr.upper())

# center ljust rjust 返回一个原字符串居中, 并使用空格填充至长度width的新字符串
# mystr.center(width)
# print(mystr.center(100))

# strip 删除字符创左右两边的空格
# print(mystr.strip())

# join 加入 于将序列中的元素以指定的字符连接生成一个新的字符串。
str=''
li=['1','2','3','4','5']
print(str.join(li))
print(type(str.join(li)))