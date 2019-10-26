l=[1,2,3,4,5,6]
def two_search(l,item):
    if len(l)==0:
        return False
    mid=len(l)//2
    if l[mid]==item:
        return True
    elif item < l[mid]:
        return two_search(l[:mid],item)
    else:
        return two_search(l[mid+1:],item)
print(two_search(l,6))
