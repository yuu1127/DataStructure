class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # rangehはiteratorsを返す(python3)
        return set(range(1, len(nums) + 1)) - set(nums)