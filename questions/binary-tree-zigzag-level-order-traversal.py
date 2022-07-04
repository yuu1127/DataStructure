# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        deque = collections.deque()
        ret = []
        if not root:
            return []
        else:
            deque.append(root)
        flag = 0
        while deque:
            level = []
            size = len(deque)
            for _ in range(size):
                node = deque.popleft()
                level.append(node.val)
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            if flag == 0:
                ret.append(level)
                flag = 1
            else:
                ret.append(level[::-1])
                flag = 0
        return ret