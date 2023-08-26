class TreeNode:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def inorder_traversal(self):

        """"Recorre el arbol de menor a mayor (left-bottom to right-top)"""
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):

        """"Recorre el arbol de top-left a right-bottom"""
        print(self.value)
        if self.left:
            self.left.inorder_traversal()
        if self.right:
            self.right.inorder_traversal()

    def postorder_traversal(self):

        """"Recorre el arbol de right-bottom a top-left """
        if self.left:
            self.left.inorder_traversal()
        if self.right:
            self.right.inorder_traversal()
        print(self.value)

    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
            return True


tree = TreeNode(10)
tree.insert(5)
tree.insert(4)
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(22)
tree.insert(11)
tree.insert(12)

tree.inorder_traversal()
print("-"*100)
tree.preorder_traversal()
print("-"*100)
tree.postorder_traversal()
print("-"*100)
print(tree.find(666))
print(tree.find(3))








