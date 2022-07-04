# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        #         self.length = 0
        #         def depth(p):
        #             if not p:
        #                 return 0
        #             left, right = depth(p.left), depth(p.right)
        #             self.length = 1 + max(left, right)
        #             return self.length
        #         depth(root)
        #         return self.length
        deque = collections.deque()
        if root:
            deque.append(root)
        level = 0
        while deque:
            size = len(deque)
            level += 1
            for _ in range(size):
                node = deque.popleft()
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
        return level
