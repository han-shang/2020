"""二叉树广度遍历和深度遍历"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    #添加
    def add(self,item):
        node = Node(item)
        #情况1：空
        if not self.root:
            self.root = node
            return
        #情况2：非空
        q = [self.root]
        while True:
            cur = q.pop(0)
            if cur.left:
                q.append(cur.left)
            else:
                cur.left = node
                return

            if cur.right:
                q.append(cur.right)
            else:
                cur.right = node
                return


    def breadth_travel(self):
        q = [self.root]
        while q:
            cur = q.pop(0)
            print(cur.value, end=' ')
            #添加左右孩子，在依次打印
            if cur.left:
                q.append(cur.left)

            if cur.right:
                q.append(cur.right)
        print()


    def pre_travel(self,node):
        if node is None:
            return
        print(node.value, end=' ')
        self.pre_travel(node.left)
        self.pre_travel(node.right)

    def mid_travel(self,node):
        if node is None:
            return
        self.mid_travel(node.left)
        print(node.value, end=' ')
        self.mid_travel(node.right)


    def last_travel(self,node):
        if node is None:
            return

        self.last_travel(node.left)
        self.last_travel(node.right)
        print(node.value, end=' ')






# if __name__ == '__main__':
#     b = BinaryTree()
#     b.add(1)
#     b.add(2)
#     b.add(3)
#     b.add(4)
#     b.add(5)
#     b.add(6)
#     b.add(7)
#     b.add(8)
#     b.add(9)
#     b.add(10)
#     b.breadch_travel()
#     # b.pre_travel(b.root)
if __name__ == '__main__':
    tree = BinaryTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.add(10)
    # 广度遍历：1 2 3 4 5 6 7 8 9 10
    tree.breadth_travel()
    # 前序遍历：1 2 4 8 9 5 10 3 6 7
    tree.pre_travel(tree.root)
    print()
    # 中序遍历:8 4 9 2 10 5 1 6 3 7
    tree.mid_travel(tree.root)
    print()
    # # 后序遍历：8 9 4 10 5 2 6 7 3 1
    tree.last_travel(tree.root)






