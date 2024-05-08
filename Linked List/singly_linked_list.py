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
                print(tmp.data)
                tmp = tmp.next

ll1 = LinkedList()
ll1.print_LL()