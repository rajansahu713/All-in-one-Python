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

    def breath_first_search(self):
        current_node = self.root
        result = []
        queue = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.value)

            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return result
    
    def dfs_pre_order(self):
        result = []
        def traverse(current_node):
            result.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return result
    
    def dfs_post_order(self):
        result = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            result.append(current_node.value)
        traverse(self.root)
        return result

    def dfs_in_order(self):
        result = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
 
            result.append(current_node.value)

            if current_node.right is not None:
                traverse(current_node.right)
            
        traverse(self.root)
        return result
    




binary_search_tree = BinarySearchTree()
binary_search_tree.add_node(47)
binary_search_tree.add_node(21)
binary_search_tree.add_node(76)
binary_search_tree.add_node(18)
binary_search_tree.add_node(27)
binary_search_tree.add_node(52)
binary_search_tree.add_node(82)


# print(binary_search_tree.breath_first_search())
# print(binary_search_tree.dfs_pre_order())
print(binary_search_tree.dfs_post_order())
