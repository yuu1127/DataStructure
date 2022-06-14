# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        queue = collections.deque()
        if p or q:
            queue.append((p, q))
        while queue:
            node_p, node_q = queue.popleft()
            if not node_p and not node_q:
                continue
            elif None in [node_p, node_q]:
                return False
            else:
                if node_p.val != node_q.val:
                    return False
                queue.append((node_p.left, node_q.left))
                queue.append((node_p.right, node_q.right))
        return True

