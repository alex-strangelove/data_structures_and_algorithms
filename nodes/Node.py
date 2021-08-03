class Node:
    # Initialize default constructor, take as parameters a value from current node, and can add the next node (optional):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    # Returns value of current node:
    def get_value(self):
        return self.value
    
    # Returns address of the next node:
    def get_next_node(self):
        return self.next_node

    # Set a new node:
    def set_next_node(self, next_node):
        self.next_node = next_node

# Define a nodes
node_a = Node(10)
node_b = Node(20)
node_c = Node(30)
node_d = Node(50)

# Connect nodes sequentially 
node_a.set_next_node(node_b)
node_b.set_next_node(node_c)
node_c.set_next_node(node_d)

print(str(node_a.get_next_node().get_value()))
print(str(node_b.get_next_node().get_value()))
print(str(node_c.get_next_node().get_value()))




