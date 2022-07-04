class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s_nums = sorted(list(set(nums)))
        count = 1
        m_count = 1
        for i in range(1, len(s_nums)):
            if s_nums[i - 1] + 1 == s_nums[i]:
                count += 1
            else:
                m_count = max(m_count, count)
                count = 1
        m_count = max(m_count, count)
        return m_count