# week03-4.py 學習計畫 Sliding Window 第3題
# Leetcode 1004. Max Consecutive Ones III
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0
        ans = 0
        tail = 0
        n = len(nums)
        for head in range(n):
            if nums[head] == 0:
                zeros += 1
                while zeros > k:
                    if nums[tail] == 0:
                        zeros -= 1
                    tail += 1
            ans = max(ans, head - tail + 1)
        return ans
