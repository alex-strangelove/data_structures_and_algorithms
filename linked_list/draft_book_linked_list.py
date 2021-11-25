class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def set_next_node(self, next_node):
        self.next_node = next_node
    
    def get_next_node(self):
        return self.next_node

class LinkedList:
    def __init__(self, head_node, value=None):
        self.head_node = Node(head_node)
        self.value = value
    
    def get_head_node(self):
        return self.head_node
    
    def set_head_node(self, new_node):
        self.head_node = new_node 

    def insert_beginning(self, new_value):
        current_node = self.get_head_node()
        new_node = Node(new_value, current_node)
        self.set_head_node(new_node)

    def nodes_list(self):
        list = ""
        head_node = self.get_head_node() # 40
        while head_node:
            if head_node.get_value() != None:
                list += str(head_node.get_value()) + "\n"
            head_node = head_node.get_next_node()
        return list
    
    def remove_node(self, value_to_rm):
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() ==  value_to_rm:
                self.head_node = current_node.get_next_node()
            current_node = current_node.get_next_node()


ll = LinkedList(10)
ll.insert_beginning(20)
ll.insert_beginning(30)
ll.insert_beginning(40)

print(ll.nodes_list())

ll.remove_node(40)
    
print(ll.nodes_list())

# node_one = Node(1)
# node_two = Node(2)
# node_tree = Node(3)

# print(node_one.get_value())        
# print(node_two.get_value())        
# print(node_tree.get_value())      

# print('-------------------------')

# node_one.set_next_node(node_tree)
# node_two.set_next_node(node_one)

# next_one = node_one.get_next_node().get_value()
# next_two = node_two.get_next_node().get_value()

# print(next_one)        
# print(next_two)