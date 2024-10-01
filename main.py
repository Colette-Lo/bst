class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value =value

class BinTree:
    def __init__(self):
        self.root = None

    def add_node(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if new_node.value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        break
                    else:
                        current_node = current_node.right

    def search_value(self, search_term):
        current_node = self.root

        found = False
        while found is False:
            if search_term < current_node.value:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    return False
            elif search_term == current_node.value:
                found = True
                return True
            else:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    return False


new_tree = BinTree()

numList = [17, 8, 4, 12, 22, 19, 14, 5, 30, 25]

for item in numList:
    new_tree.add_node(item)

print(new_tree.search_value(25))