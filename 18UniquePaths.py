# Question: https://leetcode.com/problems/unique-paths/

# Solution 1: Dynamic Programming O(NM) + O(NM)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n] * m
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

# Verdict:
# Runtime: 47 ms, faster than 15.13% of Python3 online submissions for Unique Paths.
# Memory Usage: 14.3 MB, less than 38.56% of Python3 online submissions for Unique Paths.
