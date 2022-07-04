class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        l = len(nums)
        prefix = 1
        postfix = 1
        for i in range(l):
            ans.append(prefix)
            prefix *= nums[i]
        for i in range(l - 1, -1, -1):
            ans[i] = ans[i] * postfix
            postfix *= nums[i]
        return ans