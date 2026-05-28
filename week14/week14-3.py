# week14-3.py 學習計畫 DP - 1D 第2題
# LeetCode 746. Min Cost Climbing Stairs
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def helper(i):
            if i >= len(cost): return 0
            return cost[i] + min(helper(i+1), helper(i+2))
        return min(helper(0), helper(1))
