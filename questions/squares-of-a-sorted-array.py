#import numpy as np

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #s1 = np.square(nums)
        #new_nums = list(map(lambda x: x**2, nums))
        #return sorted(new_nums)
        s2 = sorted(x*x for x in nums)
        return s2
