# week15-4b.py ¾Ç²ß­pµe DP - Multidimensional
# LeetCode 72. Edit Distance
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        a = [[0] * (n+1) for i in range(m+1)]
        for i in range(m+1): a[i][0] = i
        for j in range(n+1): a[0][j] = j
        for i in range(m):
            for j in range(n):
                a[i+1][j+1] = min(a[i][j+1], a[i+1][j], a[i][j]) + 1
                if word1[i] == word2[j]: a[i+1][j+1] = a[i][j]
        return a[m][n]
