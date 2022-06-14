# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        deque = collections.deque()
        ans = []
        if root:
            deque.append(root)
        while deque:
            sum = 0
            size = len(deque)
            for _ in range(size):
                # treeで右から入れてくるから左から取り除いていく構造が必要
                node = deque.popleft()
                sum += node.val
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            ans.append(sum / size)
        return ans