class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, new_value):
        # if binary search tree is empty, create a new node and declare it as root
        if self.root is None:
            self.root = BinaryTreeNode(new_value)
            return

        current_node = self.root
        while True:
            while new_value < current_node.data:
                current_node = current_node.left_child
                if current_node.data is None:
                    current_node
            else:
                # if newValue is greater than value of data in root, add it to right subtree and proceed recursively
                self.root.rightChild = self.insert(self.root.rightChild, new_value)


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return str(self.data)


btree = BinaryTree()
btree.insert(10)
btree.insert(9)
btree.insert(11)
btree.insert(12)
print(btree)
