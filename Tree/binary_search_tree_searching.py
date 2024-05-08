class BST:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert_node(self, data):
        if self.val is None:
            self.val = data
            return
        if data == self.val:
            return
        if data < self.val:
            if self.left:
                self.left.insert_node(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.insert_node(data)
            else:
                self.right = BST(data)

    def search_node(self, data):
        if data == self.val:
            print("Node is found")
            return
        if data < self.val:
            if self.left:
                self.left.search_node(data)
            else:
                print("Node is not found")
        else:
            if self.right:
                self.right.search_node(data)
            else:
                print("Node is not found")

root = BST(10)
lst = [2,4,3,6,5,7,9,8]
for i in lst:
    root.insert_node(i)

root.search_node(5)