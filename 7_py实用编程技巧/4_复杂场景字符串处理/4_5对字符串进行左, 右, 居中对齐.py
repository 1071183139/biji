# s = 'abc'
#
# print(s.ljust(20))
# print(s.ljust(20, '='))
# print(s.rjust(20))
# print(s.center(20))
# print(format(s, '<20'))
# print(format(s, '>20'))
# print(format(s, '^20'))




d = {
    "a": 100,
    "as": 0.01,
    "wer": 500.0,
    "cc": 12
}

# 通过map找出key的长度
print(list(map(len, d.keys())))

w = max(list(map(len, d.keys())))
for k in d:
    print(k.ljust(w), ':', d[k])