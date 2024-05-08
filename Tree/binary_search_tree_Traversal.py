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

    def preOrder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()

    def inOrder(self):
        if self.left:
            self.left.inOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.inOrder()

    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(self.val, end=' ')

root = BST(10)
lst = [6,3,1,6,98,3,7]
for i in lst:
    root.insert_node(i)

print("Preorder Traversal")
root.preOrder()

print()
print("Inorder Traversal")
root.inOrder()

print()
print("Postorder Traversal")
root.postOrder()