class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_node(self.root, value)

    def insert_node(self, cur_node, value):
        if value <= cur_node.value:
            if cur_node.left_child:
                self.insert_node(cur_node.left_child, value)
            else:
                cur_node.left_child = Node(value)
                return True
        elif value > cur_node.value:
            if cur_node.right_child:
                self.insert_node(cur_node.right_child, value)
            else:
                cur_node.right_child = Node(value)
                return True
        return False

    def find(self, cur_node, value):
        if cur_node is None:
            return None
        if value < cur_node.value:
            return self.find(cur_node.left_child, value)
        elif value > cur_node.value:
            return self.find(cur_node.right_child, value)
        else:
            return cur_node
