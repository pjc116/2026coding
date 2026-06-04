# week15-2a.py ¾Ç²ß­pµe 1143. Longest Common Subsequence
# LeetCode 62. Unique Paths
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        @cache
        def helper(i, j):
            if i == m or j == n: return 0
            if text1[i] == text2[j]: return 1 + helper(i+1, j+1)
            else: return max(helper(i, j+1), helper(i+1, j))
        return helper(0, 0)
