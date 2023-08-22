# Binary Search Tree Implementation


class BinaryTree:
    def __init__(self) -> None:
        self.root = None
    
    def __repr__(self) -> str:
        values = dict()   
        
        current_node = self.root
        if current_node is None:
            return values
        
        if current_node is not None:
            self.iterar(current_node, values)
        
    def iterar(self, current_node, dic):
        dic[current_node.data] = [current_node.left_child, current_node.right_child]
    
    
    
    def add(self, value):
        
        if self.root is None:
            self.root = Node(value)
            return
        
        current_node = self.root
        previous_node = None
        while current_node is not None:
            if value < current_node.data:
                current_node = current_node.left_child    
            else:
                current_node = current_node.right_child
        else:
            current_node = Node(value)
            


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left_child = None
        self.right_child = None

    def __repr__(self) -> str:
        return f"""           ____ {self.data} ____ 
         /              \\
       {self.left_child}            {self.right_child}
       
       """

btree = BinaryTree()
btree.add(10)
btree.root.left_child = Node(5)
btree.root.right_child = Node(15)
btree.add(12)
btree.add(5)
btree.add(1)

print(btree.root)





























































































