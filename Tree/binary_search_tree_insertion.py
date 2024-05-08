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