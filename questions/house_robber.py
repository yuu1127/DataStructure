class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        a = 0
        b = 0

        for i in range(0, n):
            if (i%2==0):
                a = max(a+nums[i], b)
            else:
                b = max(a, b+nums[i])
        return max(a, b)
