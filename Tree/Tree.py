from collections import deque


class Node:
    def __init__(self, data=-1, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


class Create_Tree:
    def __init__(self):
        self.root = Node()
        self.myQueue = deque()

    def add(self,elem):
        node = Node(elem)

        #根节点
        if self.root.data == -1:
            self.root.data = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]
            if treeNode.lchild is None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.popleft()

    def traversal_create(self,root):
        data = input()
        if data is '#':
            return None
        else:
            root.data=data
            root.lchild=self.traversal_create(root.lchild)
            root.rchild=self.traversal_create(root.rchild)
        return root

    def travelsal_tree(self,root):
        if root is None:
            return
        print(root.data)
        self.travelsal_tree(root.lchild)
        self.travelsal_tree(root.rchild)

    def stack_traversal(self,root):
        if root is None:
            return
        mystack = []
        node=root
        while node or mystack:
            while node:
                print(node.data)
                mystack.append(node)
                node=node.lchild
            node=mystack.pop()
            node=node.rchild


    def queue_traversal(self,root):
        if root is None:
            return
        q = deque()
        q.append(root)
        while q:
            node=q.pop()
            print(node.data)
            if node.lchild is not None:
                q.append(node.lchild)
            else:
                q.append(node.rchild)