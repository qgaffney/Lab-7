class Node():
    # Empty constructor
    def __init__(self, value = None, next = None, previous = None):
        # Define the node's basic properties "value", "next", "previous" and default them
        self.value = value
        self.next = None
        self.previous = None
        # Return this node
        return None

def set(self, value):
    # Set this node's value to the given value
    self.value = value
    # Return this node
    return self
    
def get_value(self):
    # Return the value of this node
    return self.value

def get_next(self):
    # Return this node's next node
    return self.next
    
def get_previous(self):
    # Return this node's previous node
    return self.previous
    
def set_next(self, next):
    # Set this node's next node
    self.next = next
    # Return this node
    return self
    
def set_previous(self, previous):
    # Set this node's previous node
    self.previous = previous
    # Return this node
    return self

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def get_prev_node(self, node):
        return node.prev
    
    def set_prev_node(self, node, previous):
        node.prev = previous

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end = " ")
            current = current.next
        print()

node_list = DoublyLinkedList()
node_list.add_to_head(18)
node_list.add_to_head(13)
node_list.add_to_head(3)

node_list.print_list()

second_node = node_list.head.next
print(node_list.get_prev_node(second_node).value)

node_list.set_prev_node(second_node, None)
print(node_list.get_prev_node(second_node))