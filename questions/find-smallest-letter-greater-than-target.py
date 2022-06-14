class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for word in letters:
            if word > target:
                return word
        return letters[0]