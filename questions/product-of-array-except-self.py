class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        re = []
        length = len(nums)
        # for i in range(len(nums)):
        #     product = 1
        #     tmp_list = nums[:i] + nums[i + 1:length]
        #     for j in range(len(tmp_list)):
        #         product *= tmp_list[j]
        #     re.append(product)
        # return re
        p = 1
        for i in range(0, length):
            re.append(p)
            p = p * nums[i]
        p = 1
        for j in range(length - 1, -1, -1):
            re[j] = re[j] * p
            p = p * nums[j]
        return re
