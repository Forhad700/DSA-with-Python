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
            if tmp.data == x:
                break
            tmp = tmp.next
        if tmp is None:
            print("Node is not present")
        else:
            newNode = Node(data)
            newNode.next = tmp.next
            tmp.next = newNode

    def insert_before(self, data, x):
        if self.head is None:
            print("Linked List is empty")
            return 
        if self.head.data == x:
            newNode = Node(data)
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
            newNode.next = tmp.next
            tmp.next = newNode

    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("Linked List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            tmp = self.head
            while tmp.next.next is not None:
                tmp = tmp.next
            tmp.next = None

    def delete_anyNode(self, x):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.data == x:
            self.head = self.head.next
            return
        tmp = self.head
        while tmp.next is not None:
            if tmp.next.data == x:
                break
            tmp = tmp.next
        if tmp.next is None:
            print("Node is not present")
            return
        tmp.next = tmp.next.next

ll1 = LinkedList()
ll1.insert_end(10)
ll1.insert_end(20)
ll1.insert_end(30)
ll1.delete_anyNode(20)
ll1.print_LL()