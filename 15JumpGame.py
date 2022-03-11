# Question: https://leetcode.com/problems/jump-game/

# Solution:
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal, i = len(nums)-1, len(nums)-1
        while i >= 0:
            if i + nums[i] >= goal:
                goal = i
            i -= 1
        return goal == 0

# Verdict:
# Runtime: 504 ms, faster than 59.02% of Python3 online submissions for Jump Game.
# Memory Usage: 15.5 MB, less than 11.96% of Python3 online submissions for Jump Game.
