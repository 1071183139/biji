# s = '  abc  123   '
# print(s)
# # 去掉两边的空白字符
# print(s.strip())
# # 去掉左边的字符
# print(s.lstrip())
# # 去掉右边的字符
# print(s.rstrip())


# s = '+++abc---'
# # 删除字符串中的多个字符
# print(s.strip('+-'))
# s = 'abc:123'
# # 删除一个区间的字符
# print(s[:3] + s[4:])



# s = '\tabc\t123\txyz'
# # 替换单个字符
# print(s.replace('\t',''))
# # 替换多个不同字符
# import re
# s = '\tabc\t123\txyz\ropt\r'
# print(re.sub('[\t\r]','',s))



# 字符串值相互替换
# s = 'abc123def456xyz'
# a = s.maketrans('abcxyz','xyzabc')
# print(s.translate(a))


# 去除 unicode 中的特殊字符　　
import sys
import unicodedata
s = 'āáǎà ōóǒò ēéěè īíǐì'
remap = {
    # ord返回ascii值
    ord('\t'): '',
    ord('\f'): '',
    ord('\r'): None
    }
# 去除\t, \f, \r
a = s.translate(remap)
'''
　　通过使用dict.fromkeys() 方法构造一个字典，每个Unicode 和音符作为键，对于的值全部为None
　　然后使用unicodedata.normalize() 将原始输入标准化为分解形式字符
　　sys.maxunicode : 给出最大Unicode代码点的值的整数，即1114111（十六进制的0x10FFFF）。
　　unicodedata.combining:将分配给字符chr的规范组合类作为整数返回。 如果未定义组合类，则返回0。
'''
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c))) #此部分建议拆分开来理解
b = unicodedata.normalize('NFD', a)
'''
　　　调用translate 函数删除所有重音符
'''
print(b.translate(cmb_chrs))






