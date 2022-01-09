# Question: https://leetcode.com/problems/jump-game/

# Solution:
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        jump = 0
        for i in range(n):
            if jump >= i:
                jump = max(jump, i + nums[i])
        return jump >= n - 1

# Verdict:
# Runtime: 504 ms, faster than 59.02% of Python3 online submissions for Jump Game.
# Memory Usage: 15.5 MB, less than 11.96% of Python3 online submissions for Jump Game.
