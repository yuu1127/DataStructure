class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chrset = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in chrSet:
                chrSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
