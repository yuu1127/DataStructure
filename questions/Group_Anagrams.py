class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            ana = "".join(sorted(list(s)))
            ans[ana].append(s)
        return ans.values()