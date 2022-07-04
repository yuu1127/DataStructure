# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # if root == None:
        #     return False
        # stack = [(root, root.val)]
        # while stack:
        #     node, val = stack.pop()
        #     if node.left == None and node.right == None and val == sum:
        #         return True
        #     if node.left:
        #         stack.append((node.left, val + node.left.val))
        #     if node.right:
        #         stack.append((node.right, val + node.right.val))
        # return False
        if not root:
            print("tomaraneeee")
            return False
        if not root.left and not root.right and root.val == sum:
            print("tomareeeee")
            return True
        sum -= root.val
        # this left is from previous return left or right so actually do left or right or different left or right
        left = self.hasPathSum(root.left, sum)
        right = self.hasPathSum(root.right, sum)
        return left or right
