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

    def delete_node(self, data):
        if self.val is None:
            print("Tree is empty")
            return
        if data < self.val:
            if self.left:
                self.left = self.left.delete_node(data)
            else:
                print("Node is not present")
        elif data > self.val:
            if self.right:
                self.right = self.right.delete_node(data)
            else:
                print("Node is not present")
        else:
            if self.left is None:
                tmp = self.right
                self = None
                return tmp
            if self.right is None:
                tmp = self.left
                self = None
                return tmp
            node = self.right
            while node.left:
                node = node.left
            self.val = node.val
            self.right = self.right.delete_node(node.val)
        return self