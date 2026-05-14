# week12-3.py ¾Ç²ß­pµe Graph - DFS
# LeetCode 547. Number of Provinces
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        def helper(now):
            visited.add(now)
            for k in range(n):
                if k not in visited and isConnected[now][k]:
                    helper(k)
        ans = 0
        for i in range(n):
            if i not in visited:
                ans += 1
                helper(i)
        return ans
