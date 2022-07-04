class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        output = 0
        for i in range(0, len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j];
                if(total == k):
                    output += 1
        return output
