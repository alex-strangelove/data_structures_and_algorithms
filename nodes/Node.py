class Node(object):
    # Initialize default constructor, take as parameters a data from current node, and can add the next node (optional):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    # Returns data of current node:
    def get_data(self):
        return self.data
    
    # Set data for a current node:
    def set_data(self, new_data):
        self.data = new_data

    
    # Returns address of the next node:
    def get_next_node(self):
        return self.next_node

    # Set a new node:
    def set_next_node(self, next_node):
        self.next_node = next_node
    
    # Check if the next node is exist:
    def has_next(self):
        if self.next_node is None:
            return False
        else:
            return True

# Define a nodes:
node_a = Node(10)
node_b = Node(20)
node_c = Node(30)
node_d = Node(50)

# Connect nodes sequentially:
node_a.set_next_node(node_b)
node_b.set_next_node(node_c)
node_c.set_next_node(node_d)

# Get datas for the next nodes:
print(str(node_a.get_next_node().get_data()))
print(str(node_b.get_next_node().get_data()))
print(str(node_c.get_next_node().get_data()))

# Check if next node is exist:
print(node_a.has_next())
print(node_d.has_next())


