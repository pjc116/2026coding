# week15-4a.py ¾Ç²ß­pµe DP - Multidimensional
# LeetCode 72. Edit Distance
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        @cache
        def helper(i, j):
            if i == m and j == n: return 0
            if i == m: return n - j
            if j == n: return m - i
            if word1[i] == word2[j]: return helper(i+1, j+1)
            #ans1 = helper(i+1, j)
            #ans2 = helper(i, j+1)
            #ans3 = helper(i+1, j+1)
            return min(helper(i+1, j), helper(i, j+1), helper(i+1, j+1)) + 1
        return helper(0, 0)
