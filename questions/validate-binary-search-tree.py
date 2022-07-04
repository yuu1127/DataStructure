# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # def isBST(node, lower, upper):
        #     if node is None:
        #         return True
        #     # current node value
        #     val=node.val
        #     if val<=lower or val>=upper:
        #         return False
        #     # if False
        #     if not isBST(node.left,lower,val):
        #         return False
        #     if not isBST(node.right,val,upper):
        #         return False
        #     # this is BST
        #     return True
        # return isBST(root,float('-inf'),float('inf'))
        stack = []
        left_child_val = float('-inf')
        while stack != [] or root is not None:
            while root != None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= left_child_val:
                return False
            left_child_val = root.val
            root = root.right
        return True
                    
        