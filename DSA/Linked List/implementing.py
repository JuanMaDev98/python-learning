class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join([str(n) for n in nodes])

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def add_last(self, value):
        current_node = self.head
        if current_node is None:
            self.head = Node(value)
            return
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = Node(value)

    def add_after(self, target_value, node_value):
        if self.head is None:
            raise Exception("List is empty")

        current_node = self.head
        new_node = Node(node_value)

        for node in self:
            if node.data == target_value:
                new_node.next = node.next
                node.next = new_node
                return
        del new_node
        raise Exception(f"Node with data '{target_value}' not found")

    def add_before(self, target_node_data, node_value):
        if self.head is None:
            raise Exception("List is empty")

        new_node = Node(node_value)

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        del new_node
        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)





llist = LinkedList()

first_node = Node("a")
llist.head = first_node

second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node

llist2 = LinkedList([1, 2, 3, 4, 5, 6])
print(llist2)

llist2.add_first(1)
llist2.add_last(10)
llist2.add_after(4, 44)
llist2.add_before(4, 33)
llist2.remove(6)
x = 0
for node in llist2:
    print(f"Node -> {node}")
    x += node.data
    print(x)
