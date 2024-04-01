class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if prev_node is None:
            raise ValueError("Previous node must be in the DoublyLinkedList.")
        new_node = Node(data)
        new_node.prev = prev_node
        new_node.next = prev_node.next
        if prev_node.next:
            prev_node.next.prev = new_node
        prev_node.next = new_node

    def delete_head(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_tail(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.prev.next = None

    def delete_middle(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data and current_node.next is not None:
                if current_node == self.head:
                    self.head = current_node.next
                    current_node.next.prev = None
                    return
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
                return
            current_node = current_node.next

    def display_forward(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("None")

    def display_backward(self):
        current_node = self.head
        while current_node and current_node.next:
            current_node = current_node.next
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.prev
        print("None")

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.display_forward()
dll.prepend(0)
dll.display_forward()
dll.insert_after_node(dll.head.next, 4)
dll.display_forward()
dll.delete_head()
dll.display_forward()
dll.delete_middle(4)
dll.display_forward()
dll.delete_tail()
dll.display_forward()
