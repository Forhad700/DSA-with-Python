class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            tmp = self.head
            while tmp is not None:
                print(tmp.data, end=' ')
                tmp = tmp.next

    def insert_begin(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
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

    def insert_after(self, data, x):
        tmp = self.head
        while tmp is not None:
            if x == tmp.data:
                break
            tmp = tmp.next
        if tmp is None:
            print("Node is not present")
        else:
            newNode = Node(data)
            newNode.next = tmp.next
            tmp.next = newNode

ll1 = LinkedList()
ll1.insert_end(10)
ll1.insert_end(20)
ll1.insert_begin(30)
ll1.insert_after(40,20)
ll1.print_LL()