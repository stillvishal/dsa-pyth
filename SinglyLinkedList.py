class Node:
    def __init__(self, info, next = None):
        self.data = info
        self.next = next

class SinglyLinkedList:
    def __init__(self, head = None):
        self.head = head
    def insertAtEnd(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node