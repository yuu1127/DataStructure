class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        ans = []
        length = len(text)
        for i in range(length):
            for j in range(i, length + 1):
                # caz if 0..7 then print 0..6
                if text[i:j] in words:
                    ans.append([i,j - 1])
        return ans
