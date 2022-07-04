from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = defaultdict(list)
        ans = []
        for n in nums:
            count[n] += 1
        for n,c in count.items():
            freq[c].append(n)
        for i in sorted(freq.keys(), reverse=True):
            for j in freq[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans