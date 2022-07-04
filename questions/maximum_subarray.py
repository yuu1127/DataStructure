i
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            # 記録しておいて
            # negativeになったら次のものから始めた方が良い
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)