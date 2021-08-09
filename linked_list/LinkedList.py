# Create Node object:
class Node(object):
    

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def to_string(self):
        return "Node value: " + str(self.data)

    def has_next(self):
        if self.get_next_node() is None:
            return False
        else:
            return True
    def compare_to(self, y):
        if self.to_string() < y.to_string():
            return -1
        elif self.to_string() > y.to_string():
            return 1
        return 0

# Below is way to implement Linked Lists in Python:
class LinkedList(object):

    # Default constructor take parameter of value node:
    def __init__(self, value=None):
        self.value = value
        self.head_node = Node(value)
        self.size = 0

    # Returns linked list size:
    def get_size(self):
        return self.size
    
    # Returns linked list size in string representation:
    def get_size_str(self):
        return "Size of linked list is: " + str(self.size)

    def get_head_node(self):
        return self.head_node
        
    # Adding a new node:
    def insert_beginning(self, new_value):
        new_node = Node(new_value, self.head_node)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
        self.size += 1
    


    # Remove node from linked list:
    def remove_node(self, data):
        current_node = self.head_node
        prev_node = None
        while current_node:
            if current_node.get_data() == data:
                if prev_node: # Removing node that is not the value
                    prev_node.set_next_node(current_node.get_next_node())
                else: # Removing value node
                    self.head_node = current_node.get_next_node()
                    self.size -= 1
                    return True # Data has been removed
            else:
                prev_node = current_node
                current_node = current_node.get_next_node()
                return False # Data not found
            return False


    # Find a node:
    def find_node(self, data):
        current_node = self.head_node

        while current_node:
            if current_node.get_data() == data:
                return "Node has been found: " + str(data)
            else:
                current_node = current_node.get_next_node()
        return None
    
    # Print list nodes:
    def print_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node.has_next():
            if current_node.get_data() != None:
                string_list += str(current_node.get_data()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

def list_debug():
    # Create an linked list:
    my_list = LinkedList()

    # Fill the list with values:
    my_list.insert_beginning("Node 1")
    my_list.insert_beginning("Node 2")
    my_list.insert_beginning("Node 3")
    my_list.insert_beginning("Node 4")
    my_list.insert_beginning("Node 5")

    # Print list of nodes:
    print("\n***DEBUG*** ---Prints list of nodes:\n")
    print(my_list.print_list())

    # Remove value:
    my_list.remove_node("Node 1")

    # Print list of nodes after removing:
    print("\n***DEBUG*** ---Prints list of nodes after removing:\n")
    print(my_list.print_list())

    # Prints head(root) node:
    print("\n***DEBUG*** ---Prints the root head node:\n")
    print(my_list.get_head_node().get_data())

    # Prints the size of list nodes:
    print("\n***DEBUG*** ---Prints the size of linked list:\n")
    print(my_list.get_size_str())

# Create a linked list for user_list():
my_list1 = LinkedList()
# Define method for user management:
def user_list():
    print("\n___---*** Welcome to the linked list management system ***---___")
    print(""" 
    \nAvaiable operations:\n
    1.Add new node\n
    2.Remove node by value\n
    3.Get size of linked list\n
    4.Print linked list\n
    5.Find node by value\n
    6.Exit programm 
    """)
    usr_in = input("Please enter the number of operation: ")
    

    if usr_in == '1':
        print("You're going to add a new node")
        usr_in = input("Please enter a value of new node: ")
        my_list1.insert_beginning(usr_in)
        input("Hit any key to continue...")
        user_list()

    elif usr_in == '2':
        print("Removing a node by value\n")
        usr_in = input("Please enter value to delete: ")
        if my_list1.remove_node(usr_in):
            print("Node {value} has been removed!".format(value=usr_in))
            input("Hit any key to continue...")
            user_list()
        else:
            print("Entered value does not exist!")
            input("Hit any key to continue...")
            user_list()

    elif usr_in == '3':
        print(my_list1.get_size_str())
        input("Hit any key to continue...")
        user_list()

    elif usr_in == '4':
        print("List of known nodes:")
        print(my_list1.print_list())
        input("Hit any key to continue...")
        user_list()
    
    elif usr_in == '5':
        usr_in = input("Please enter node to find: ")
        print(my_list1.find_node(usr_in))
        input("Hit any key to continue...")
        user_list()

    elif usr_in == '6':
        print("Exit of the program....")
        input("Hit any key to continue...")
        return

    else:
        print("Please enter the correct value!")
        input("Hit any key to and try again...")
        user_list()



# Functional Test:
def main():
    # list_debug() # -- Optional: you can uncomment this row for debugging
    user_list()

main()

