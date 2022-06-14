#Given an integer array arr that is guaranteed to be a mountain,
#return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        #return arr.index(max(arr))
        l, r = 0, len(arr) - 1
        while l != r:
            m = (l + r) // 2
            if arr[m] < arr[m + 1]:
                l = m + 1
            else:
                r = m
        # or return l
        return r
