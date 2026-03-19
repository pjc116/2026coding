# week04-4b.py (­«¼g week04-3.py)
# LeetCode 724. Find Pivot Index
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        h = [0 * 200]
        for nn in nums:
            h[nn] += 1
        for nn in nums:
            if nn % 2 == 0 and h[nn] == 1:
                return nn
        return -1
