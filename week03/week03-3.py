# week03-3.py 學習計畫 Sliding Window 第2題
# Leetcode 1456. Maximum Number of Vowels in a Substring of Given Length
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou') # 把5個字母，變set()
        count = 0 # 計數器
        for i in range(k): # 找k個字母
            if s[i] in vowels: count += 1
        ans = count
        n = len(s)
        for i in range(k, n):
            if s[i] in vowels: count += 1
            if s[i-k] in vowels: count -= 1
            ans = max(ans, count)
        return ans
