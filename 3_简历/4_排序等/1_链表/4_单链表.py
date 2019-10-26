

class SinglinkNode(object):
    # 创建节点
    def __init__(self,item):
        self.item=item
        self.next=None

class SingLink(object):
    def __init__(self):
        self.__head=None

    # 链表的长度
    def length(self):
        count=0
        cur=self.__head
        while cur is not None:
            count+=1
            cur=cur.next
        return count

    # 判断链表是否为空
    def is_empty(self):
        if self.__head is not None:
            return True
        return False

    # 循环链表
    def travel(self):
        cur=self.__head
        while cur is not None:
            print(cur.item,end=" ")
            cur=cur.next
        print('')

    # 向链表的头部添加
    def add(self,item):
        node=SinglinkNode(item)
        node.next=self.__head
        self.__head=node

    # 向链表的尾部添加
    def append(self,item):
        node=SinglinkNode(item)
        if self.is_empty():
            self.__head=node
        else:
            cur = self.__head
            while cur.next is not None:
                cur=cur.next
            cur.next=node

    # 向指定位置添加
    def insert(self,pos,item):
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            count=0
            node=SinglinkNode(item)
            pre=self.__head
            while count < pos-1:
                count+=1
                pre=pre.next
            node.next=pre.next
            pre.next=node

    # 删除链表的元素
    def remove(self,item):
        cur=self.__head
        pre=None
        while cur is not None:
            if cur.item==item:
                if pre is None:
                    self.__head=cur.next
                else:
                    pre.next=cur.next
            pre=cur
            cur=cur.next


    # 查找元素
    def search(self,item):
        cur=self.__head
        while cur is not None:
            if cur.item == item:
                return True
            return False

if __name__ == '__main__':
    ll=SingLink()
    # ll.add(3)
    # ll.add(156)
    ll.append(789)
    ll.add(1)
    ll.append(17)
    ll.insert(4, 222)
    ll.travel()
    ll.remove(17)
    ll.travel()
    lens=ll.length()
    print("链表的长度:%d"%lens)
    print(ll.search(17))