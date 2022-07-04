from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
            if dic[num] > length / 2:
                return num
        # res, count = 0, 0
        # for n in nums:
        #     if count == 0:
        #         res = n
        #     count += (1 if n == res else -1)
        # return res
