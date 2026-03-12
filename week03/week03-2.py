# week03-2.py 學習計畫 Sliding Window 第1題
# LeetCode 643. Maximum Average Subarray I
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        total = sum(nums[:k]) # sum = 加總 [:k] 前k項
        maxTotal = total
        for i in range(k, n):
            total = total + nums[i] - nums[i-k]
            maxTotal = max(maxTotal, total)
        return maxTotal / k
