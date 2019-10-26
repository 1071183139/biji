class Node(object):
    """树的节点类"""
    def __init__(self, item):

        self.item = item
        # 左子节点
        self.lChild = None
        # 右子节点
        self.rChild = None


class Tree(object):

    def __init__(self):
        # 初始化根节点
        self.__root = None

    def add(self, item):
        """添加节点"""
        node = Node(item)
        # 判断是否为空
        if self.__root is None:
            self.__root = node
        else:
            # 以队列的方式，找新节点的位置
            queue = []
            queue.append(self.__root)

            while queue:
                q_node = queue.pop(0)
                if q_node.lChild is None: # 左节点为空
                    q_node.lChild = node
                    return
                if q_node.rChild is None: # 右节点为空
                    q_node.rChild = node
                    return
                # 左右子节点都有数据
                queue.append(q_node.lChild)
                queue.append(q_node.rChild)

    # 广度优先遍历 层次遍历
    def breth_travel(self):
        if self.__root is None:
            return

        queue = []
        queue.append(self.__root)

        while queue:
            node = queue.pop(0)
            print(node.item)

            if node.lChild is not None:
                queue.append(node.lChild)
            if node.rChild is not None:
                queue.append(node.rChild)

    def depth_travel(self):
        # self.preorder(self.__root)
        # self.inorder(self.__root)
        self.postorder(self.__root)
    #  先序
    # def preorder(self, node):
    #     if node is None:
    #         return
    #     print(node.item,end=" ")
    #     self.preorder(node.lChild)
    #     self.preorder(node.rChild)

    # 中序
    # def inorder(self, node):
    #     if node is None:
    #         return
    #     self.inorder(node.lChild)
    #     print(node.item,end=" ")
    #     self.inorder(node.rChild)

    # 后续
    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.lChild)
        self.postorder(node.rChild)
        print(node.item,end=" ")



if __name__ == '__main__':
    tree = Tree()
    tree.add(9)
    tree.add(8)
    tree.add(7)
    tree.add(6)
    tree.add(5)
    tree.add(4)
    tree.add(3)
    tree.add(2)
    tree.add(1)
    tree.add(0)
    # tree.breth_travel()
    tree.depth_travel()