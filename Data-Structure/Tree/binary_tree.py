class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add_node(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while(True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            


    def node_check(self, value):
        if self.root is None:
            return None
        if self.root.value == value:
            return True
        temp = self.root
        while(temp):
            if value < temp.value:
                if temp.left is not None:
                    if value == temp.left.value:
                        return True
                    temp = temp.left
                else:
                    return False
            else:
                if temp.right is not None:
                    if value == temp.right.value:
                        return True
                    temp = temp.right
                else:
                    return False  
    
    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        
        if value == current_node.value:
            return True
        
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        
    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    

    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)

        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)

        return current_node
    
    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)


            



    def print_tree(self):
        pass
        





binary_search_tree = BinarySearchTree()
# binary_search_tree.add_node(47)
# binary_search_tree.add_node(21)
# binary_search_tree.add_node(76)
# binary_search_tree.add_node(18)
# binary_search_tree.add_node(27)
# binary_search_tree.add_node(52)
# binary_search_tree.add_node(82)
binary_search_tree.r_insert(5)
binary_search_tree.r_insert(4)
binary_search_tree.r_insert(7)

print(binary_search_tree.root.value)
print(binary_search_tree.root.left.value)
print(binary_search_tree.root.right.value)

# print(binary_search_tree.root.right.value)
# print(binary_search_tree.node_check(3))

# print(binary_search_tree.r_contains(27))

# print(binary_search_tree.r_contains(17))
