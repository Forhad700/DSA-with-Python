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

    def print_LL(self):
        if self.head is None:
            print("Linked List is empty")
            return
        tmp = self.head
        while tmp is not None:
            print(tmp.data, end=' ')
            tmp = tmp.next

    def print_LL_Reverse(self):
        if self.head is None:
            print("Linked List is empty")
            return
        tmp = self.head
        while tmp.next is not None:
            tmp = tmp.next
        while tmp is not None:
            print(tmp.data, end=' ')
            tmp = tmp.prev

ll = Doubly_LL()
ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)

ll.print_LL_Reverse()