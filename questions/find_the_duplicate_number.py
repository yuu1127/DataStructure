from collections import defaultdict

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
            if dic[i] > 1:
                return i
