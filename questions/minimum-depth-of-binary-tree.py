# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        deque = collections.deque()
        level = 0
        if root:
            deque.append(root)
        while deque:
            level += 1
            size = len(deque)
            for _ in range(size):
                node = deque.popleft()
                if node.left == None and node.right == None:
                    return level
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
        return 0