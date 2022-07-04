# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.length = 0

        def depth(p):
            if not p:
                return 0
            left, right = depth(p.left), depth(p.right)
            self.length = max(self.length, left + right)
            return 1 + max(left, right)

        depth(root)
        return self.length
