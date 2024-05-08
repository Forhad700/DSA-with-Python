class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Doubly_LL:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def insert_end(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            tmp = self.head
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = newNode
            newNode.prev = tmp

    def insert_after(self, data, x):
        tmp = self.head
        while tmp is not None:
            if tmp.data == x:
                break
            tmp = tmp.next
        if tmp is None:
            print("Node is not present")
        elif tmp.next is None:
            newNode = Node(data)
            tmp.next = newNode
            newNode.prev = tmp
        else:
            newNode = Node(data)
            tmp.next.prev = newNode
            newNode.next = tmp.next
            tmp.next = newNode
            newNode.prev = tmp

    def insert_before(self, data, x):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.data == x:
            newNode = Node(data)
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            return
        tmp = self.head
        while tmp.next is not None:
            if tmp.next.data == x:
                break
            tmp = tmp.next
        if tmp.next is None:
            print("Node is not present")
        else:
            newNode = Node(data)
            tmp.next.prev = newNode
            newNode.next = tmp.next
            tmp.next = newNode
            newNode.prev = tmp

    def insert_empty(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            print("Linked List is not empty")

    def print_LL(self):
        if self.head is None:
            print("Linked List is empty")
            return
        tmp = self.head
        while tmp is not None:
            print(tmp.data, end=' ')
            tmp = tmp.next

ll = Doubly_LL()
ll.print_LL()