from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # for i in nums:
        #     if nums.count(i) == 1:
        #         return i
        # return None
        hashs = defaultdict(int)
        for i in nums:
            hashs[i] += 1
        for i in hashs:
            if hashs[i] == 1:
                return i
