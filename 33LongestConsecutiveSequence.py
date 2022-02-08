# Question: https://leetcode.com/problems/longest-consecutive-sequence/

# -------------------------------------------------------------------------------------------------------- #

# Solution 1: Brute Force: Sort and compare
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        ans = 1
        curr = 1
        for i in range(0, len(nums)):
            if nums[i] - nums[i-1] == 1:
                curr += 1
                ans = max(ans, curr)
            elif nums[i] == nums[i-1]:
                continue
            else:
                curr = 1
        return ans

# Verdict:
# Runtime: 216 ms, faster than 76.70% of Python3 online submissions for Longest Consecutive Sequence.
# Memory Usage: 23.3 MB, less than 92.43% of Python3 online submissions for Longest Consecutive Sequence.

# -------------------------------------------------------------------------------------------------------- #
