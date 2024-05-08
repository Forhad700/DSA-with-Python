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

    def delete_node(self, data, cur):
        if self.val is None:
            print("Tree is empty")
            return
        if data < self.val:
            if self.left:
                self.left = self.left.delete_node(data, cur)
            else:
                print("Node is not present")
        elif data > self.val:
            if self.right:
                self.right = self.right.delete_node(data, cur)
            else:
                print("Node is not present")
        else:
            if self.left is None:
                tmp = self.right
                if data == cur:
                    self.val = tmp.val
                    self.left = tmp.left
                    self.right = tmp.right
                    tmp = None
                    return
                self = None
                return tmp
            if self.right is None:
                tmp = self.left
                if data == cur:
                    self.val = tmp.val
                    self.left = tmp.left
                    self.right = tmp.right
                    tmp = None
                    return
                self = None
                return tmp
            node = self.right
            while node.left:
                node = node.left
            self.val = node.val
            self.right = self.right.delete_node(node.val, cur)
        return self
    
    def preOrder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()

def count_node(node):
        if node is None:
            return 0
        return 1 + count_node(node.left) + count_node(node.right)
    
root = BST(10)
lst = [1,12]
for i in lst:
    root.insert_node(i)

print("Preorder")
root.preOrder()
print()

if count_node(root)>1:
    root.delete_node(10, root.val)
else:
    print("Can't Delete! More than 1 node need")

print("after Deleting")
root.preOrder()