class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #a[0:len(a)],a[:],a[::] 全ての要素指定
        for i in range(k):
            nums[:] = [nums[-1]] + nums[:-1]