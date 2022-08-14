

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.next = None

    def add(self, data):
        ''' Adding the element to the list
        :param data - value to be added in the list
        '''
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def traverse(self):
        '''
        Iterate and yields the element value from the list
        :return: None
        '''
        cur = self.head
        while cur != None:
            yield cur.data
            cur = cur.next

    def search(self, value):
        '''
        Search the given value in the list
        :param value: searchable value
        :return: boolean true or false
        '''
        cur = self.head
        while cur != None and cur.data != value:
            cur = cur.next
        if cur is None:
            return False
        return True

    def remove(self, value):
        '''
        Removing the node that matches the given value
        :param value:
        :return: Boolean, true or false
        '''
        if self.head is None: # Case 1: The list is empty
            return False
        cur = self.head
        if cur.data == value:
            if self.head == self.tail: # Case 2: whether there is only one node in the list
                self.head = None
                self.tail = None
            else: # Case 3: We are removing the head node
                self.head = self.head.next
            return True
        else:
            while cur.next != None and cur.next.data != value:
                cur = cur.next
            if cur.next != None:
                if cur.next == self.tail: # Case 4: We are removing the tail node
                    self.tail = cur
                else: # Case 5: Removing the node somewhere between head and tail
                    cur.next = cur.next.next
                return True
        return False # Case 6: The item does not exist in the list

    def reverse_traverse(self):
        '''
        Reverse traversal is not efficient in singly linkedlist-O(n2) is the worst order
        :return:
        '''
        if self.tail != None:
            cur = self.tail
            while cur != self.head:
                prev = self.head
                while prev.next != cur:
                    prev = prev.next
                yield cur.data
                cur = prev
            yield cur.data
        else:
            return None


class DoublyLinkedList:
    """
    Doubly linkedlist is similar to singly linked list except Insertion and Deletion algorithm
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        '''
        Value will be placed at the tail of the list
        :param data:
        :return:
        '''
        new_node = DoubleNode(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node


    def traverse(self):
        '''
        Forward traversal to the nodes of the list and return value
        :return:
        '''
        cur = self.head

        while cur != None:
            yield cur.data
            cur = cur.next

    def reverse_traverse(self):
        '''
        Reversal in doubly linkedlist is efficient than singly linkedlist
        :return:
        '''
        cur = self.tail
        while cur != None:
            yield cur.data
            cur = cur.prev

    def remove(self, value):
        '''
        Remove a node is similar to singly linkedlist
        :return:
        '''
        if self.head is None:
            return False

        if self.head.data == value:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return True
        else:
            cur = self.head.next

            while cur != None and cur.data != value:
                cur = cur.next
            if cur == self.tail:
                self.tail = self.tail.prev
                self.tail.next = None
                return True
            elif cur != None:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                return True
        return False





