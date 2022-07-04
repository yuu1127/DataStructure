# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
na
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = collections.deque()
        if root:
            queue.append(root)
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     if node:
        #         node.left, node.right = node.right, node.left
        #         stack.append(node.right)
        #         stack.append(node.left)
        # return root
