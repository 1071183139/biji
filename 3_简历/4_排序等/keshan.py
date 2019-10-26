# 主要的思想是从中间开始，大的网右边查找，小的往左边查找，依次递归

def search(li,item):
    if len(li) == 0:
        return False
    mid = len(li)//2
    if item == mid:
        return True
    if item > li[mid]:
        return search(li[mid+1:],item)
    else:
        return search(li[:mid,item])


if __name__ == '__main__':
    li = [1,2,3,4,5]
    print(search(li,2))
    print(search(li,6))