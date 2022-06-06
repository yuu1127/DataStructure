# Written by Yuta

from copy import deepcopy

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next_node = None

class LinkedList:
    def __init__(self, L = None):
        if L is None:
            self.head = None
            return
        if not len(L[: 1]):
            self.head = None
            return
        node = Node(L[0])
        self.head = node
        for e in L[1: ]:
            node.next_node = Node(e)
            node = node.next_node

    def print(self, separator = ', '):
        if not self.head:
            return
        nodes = []
        node = self.head
        while node:
            nodes.append(str(node.value))
            node = node.next_node
        print(separator.join(nodes))

    def duplicate(self):
        if not self.head:
            return
        node = self.head
        node_copy = Node(deepcopy(node.value))
        L = LinkedList(key = self.key)
        L.head = node_copy
        node = node.next_node
        while node:
            node_copy.next_node = Node(deepcopy(node.value))
            node_copy = node_copy.next_node
            node = node.next_node
        return L

    def __len__(self):
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next_node
        return length

    def is_sorted(self):
        node = self.head
        while node and node.next_node:
            if node.value > node.next_node.value:
                return False
            node = node.next_node
        return True

    def reverse(self):
        if not self.head:
            return
        node = self.head.next_node
        self.head.next_node = None
        while node:
            next_node = node.next_node
            node.next_node = self.head
            self.head = node
            node = next_node

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        node = self.head
        while node.next_node:
            node = node.next_node
        node.next_node = Node(value)

    def delete_value(self, value):
        if not self.head:
            return False
        if self.head.value == value:
            self.head = self.head.next_node
            return True
        node = self.head
        while node.next_node and node.next_node.value != value:
            node = node.next_node
        if node.next_node:
            node.next_node = node.next_node.next_node
            return True
        return False
