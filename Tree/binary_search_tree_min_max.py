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

    def min_node(self):
        curr = self
        while curr.left:
            curr = curr.left
        print("Min Node value is: ", curr.val)

    def max_node(self):
        curr = self
        while curr.right:
            curr = curr.right
        print("Max Node value is: ", curr.val)

root = BST(10)
lst = [6,3,1,6,98,3,7,100]
for i in lst:
    root.insert_node(i)

root.min_node()
root.max_node()