# Written by Yuta

class BinaryTree:
    def __init__(self, value = None):
        self.value = value
        if self.value is not None:
            self.left_node = BinaryTree()
            self.right_node = BinaryTree()
        else:
            self.left_node = None
            self.right_node = None

    def height(self):
        if self.value is Nonw:
            return 0
        return max(self.left_node._height(), self.right_node._height())

    def _height(self):
        if self.value is None:
            return 0
        return max(self.left_node._height(), self.right_node()._height()) + 1

    def size(self):
        if self.value is None:
            return 0
        return 1 + self.left_node.size() + self.right_node.size()

    def insert_in_bst(self, value):
        if self.value is None:
            self.value = value
            self.left_node = BinaryTree()
            self.right_node = BinaryTree()
            return True
        if self.value == value:
            return False
        if value < self.value:
            return self.left_node.insert_in_bst(value)
        return self.right_node.insert_in_bst(value)