
#最基本的冒泡
def mao1(li):

    n=len(li)
    #循环几遍排序
    for j in range(n):
        #循环第一遍比较两两数
        for i in range(n-1):#(必须-1,3个数相比较2次就可以了)
            if li[i] > li[i+1]:
                li[i],li[i+1]=li[i+1],li[i]
    print(li)

li=[5,4,3,2,1,6,9,8,7]
mao1(li)



#有三个优化的冒牌排序
def mao2(li):
    n = len(li)

    #(优化1：-1,5个数4个都找到位置就可以了)
    for j in range(n-1):

        #(优化三，如果循环一遍，要换位置count+1，不换位置count=0说明没有要换的。
        #不走第二遍排序 )
        count=0

        #(优化2:-i,减循环次数)
        for i in range(n - 1-j):
            if li[i] > li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]
                count += 1

        if count == 0:
            break

    print(li)


list = [3, 2, 1]
mao2(list)
