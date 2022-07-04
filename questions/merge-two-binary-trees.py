# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        deque1 = collections.deque()
        deque1.append(t1)
        deque2 = collections.deque()
        deque2.append(t2)
        while deque1 and deque2:
            size = len(deque1)
            for _ in range(size):
                node1 = deque1.popleft()
                node2 = deque2.popleft()
                if node1 and node2:
                    node1.val = node1.val + node2.val
                    if not node1.left and node2.left:
                        node1.left = TreeNode(0)
                    if not node1.right and node2.right:
                        node1.right = TreeNode(0)
                    deque1.append(node1.left)
                    deque1.append(node1.right)
                    deque2.append(node2.left)
                    deque2.append(node2.right)
        return t1
