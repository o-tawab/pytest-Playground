class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node

    def remove_node(self, index):
        prev = None
        node = self.head
        i = 0

        while node is not None and i < index:
            prev = node
            node = node.next
            i += 1

        if prev is None:
            self.head = node.next
        else:
            prev.next = node.next

    def search(self, key):
        node = self.head
        i = 1

        while node is not None:
            if node.data == key:
                return i
            i += 1
            node = node.next

        return -1

    def as_list(self):
        l = []
        node = self.head

        while node is not None:
            l.append(node.data)
            node = node.next
        return l
