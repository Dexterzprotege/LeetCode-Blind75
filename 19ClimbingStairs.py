# Question: https://leetcode.com/problems/climbing-stairs/

# Solution:
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2]
        for i in range(1, 46):
            dp.append(dp[-1] + dp[-2])
        return dp[n]

# Verdict:
# Runtime: 59 ms, faster than 5.15% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 14.2 MB, less than 44.84% of Python3 online submissions for Climbing Stairs.
