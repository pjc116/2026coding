# week04-4c.py (­«¼g week04-4b.py)
# LeetCode 3866. First Unique Even Element
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        h = Counter(nums)
        for nn in nums:
            if nn % 2 == 0 and h[nn] == 1:
                return nn
        return -1
