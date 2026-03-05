# week02-3.py 學習計畫 Two Pointers 第2題
# LeetCode 392. Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n1, n2 = len(s), len(t)
        if n1 == 0:
            return True
        i = 0
        for k in range(n2):
            if s[i] == t[k]: # 找左右符合
                i += 1 # 左邊 i 升一級
        if i == n1:
            return True
        else:
            return False
