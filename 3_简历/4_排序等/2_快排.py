# 快排，找一个数做比较，左边的数要比它小，右边的数要比它大。
# 比较一次，就能找到一个数正确的位置。（小的跑到比较前面，大的跑到比较后边。步子比较大）

def qucik_sort(li,start,end):
    # 递归的退出条件
    if start >= end:
        return
    left = start
    right = end
    mid = li[left]

    while left < right:
        # 右边的索引往左移动，当右边的值小于mid的时候，把值赋值给left索引
        while left < right and li[right] >= mid:
            right -= 1
        li[left] = li[right]

        # 左边的索引往右移动，当左边的值大于mid的时候，把值赋值给right索引
        while left < right and li[left] < mid:
            left += 1
        li[right] = li[left]
    li[left] = mid

    # 递归
    # mid左边的数排序
    qucik_sort(li,0,left-1)
    # mid的右边的数排序
    qucik_sort(li,left+1,end)
    return li
li = [7,4,2,5,3,1]
print(qucik_sort(li,0,len(li)-1))