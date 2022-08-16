from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        '''
        Value has passed custom check for type T
        :param value:
        :return:
        '''
        if self.root is None:
            self.root = Node(value)
        else:
            self.insertNode(self.root, value)

    def insertNode(self, current, value):
        '''
        Current is the node to start from
        :param current:
        :param value:
        :return:
        '''
        if value < current.data:
            if current.left is None:
                current.left = Node(value)
            else:
                self.insertNode(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self.insertNode(current.right, value)

    def preOrder(self, curr):
        '''
        Root is the root of the BST
        the nodes in the BST have been visited in preorder
        :return:
        '''
        if curr is not None:
            print(curr.data)
            self.preOrder(curr.left)
            self.preOrder(curr.right)
        else:
            return False

    def postOrder(self, curr):

        if curr is not None:
            self.postOrder(curr.left)
            self.postOrder(curr.right)
            print(curr.data)

    def inOrder(self, curr):

        if curr != None:
            self.inOrder(curr.left)
            print(curr.data)
            self.inOrder(curr.right)

    def findMin(self, current):
        '''
        Root is the root node of the BST
        :return: Smallest value in the BST
        '''
        if current.left is None:
            return current.data

        return self.findMin(current.left)

    def findMax(self, current):
        '''
        Search the BST and find the max
        :param current:
        :return:
        '''
        if current.right is None:
            return current.data

        return self.findMax(current.right)


    def findNode(self, current, value):
        '''
        Value is the value of the node
        :param value:
        :return: a reference of the found node will be returned
        '''
        if current is None:
            return None

        if current.data == value:
            return current
        elif value < current.data:
            return self.findNode(current.left, value)
        else:
            return self.findNode(current.right, value)

    def bredthFirst(self, current):
        que = deque()
        visited = []
        while current != None:
            visited.append(current.data)
            if current.left != None:
                que.append(current.left)
            if current.right != None:
                que.append(current.right)
            if que:
                current = que.popleft()
            else:
                current = None
        return visited

