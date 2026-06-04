# week15-2b.py ¾Ç²ß­pµe 1143. Longest Common Subsequence
# LeetCode 62. Unique Paths
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        table = [[0] * (n+1) for i in range(m+1)]

        for i in range(m):
            for j in range(n):
                #case1 = table[i-1][j]
                #case2 = table[i][j-1]
                #case3 = table[i-1][j-1] + 1
                if text1[i] == text2[j]: table[i+1][j+1] = table[i][j] + 1
                table[i+1][j+1] = max(table[i+1][j+1], table[i][j+1], table[i+1][j])
        return table[m][n]
