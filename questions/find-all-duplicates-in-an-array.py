from collections import defaultdict

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic = defaultdict(int)
        re = []
        for i in nums:
            dic[i] += 1
        for k in dic.keys():
            if dic[k] == 2:
                re.append(k)
        return sorted(re)
