# Question: https://leetcode.com/problems/longest-consecutive-sequence/

# -------------------------------------------------------------------------------------------------------- #

# Solution 3: Same as Sol 2, but cleaner
class Solution:
    def longestConsecutive(self, nums):
        nums = set(nums)
        ans = 0
        for i in nums:
            if i - 1 not in nums:
                x = i + 1
                while x in nums:
                    x += 1
                ans = max(ans, x - i)
        return ans
    
# Verdict:
# Runtime: 176 ms, faster than 98.54% of Python3 online submissions for Longest Consecutive Sequence.
# Memory Usage: 27.5 MB, less than 35.44% of Python3 online submissions for Longest Consecutive Sequence.

# -------------------------------------------------------------------------------------------------------- #

# Solution 2: Set approach, add to set compare left and right
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        ans = 0
        for i in nums:
            # If we found left element we just continue
            if i-1 not in numSet:
                length = 0
                # Computing answer until we reach the consective limit
                while i+length in numSet:
                    length += 1
                ans = max(ans, length)
        return ans
    
# Verdict:
# Runtime: 2547 ms, faster than 19.43% of Python3 online submissions for Longest Consecutive Sequence.
# Memory Usage: 27.7 MB, less than 24.75% of Python3 online submissions for Longest Consecutive Sequence.

# -------------------------------------------------------------------------------------------------------- #

# Solution 1: Brute Force: Sort and compare
class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        nums = sorted(nums)
        ans, curr = 1, 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1] + 1:
                    curr += 1
                else:
                    ans = max(ans, curr)
                    curr = 1
        return max(ans, curr)

# Verdict:
# Runtime: 365 ms, faster than 44.84% of Python3 online submissions for Longest Consecutive Sequence.
# Memory Usage: 23.5 MB, less than 90.94% of Python3 online submissions for Longest Consecutive Sequence.
# -------------------------------------------------------------------------------------------------------- #
