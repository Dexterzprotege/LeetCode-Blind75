# Question: https://leetcode.com/problems/maximum-subarray/

# Solution 2: Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a = nums[0] # Max here
        b = nums[0] # Max overall
        for i in range(1, len(nums)):
            a = max(a+nums[i], nums[i])
            b = max(a, b)
        return b

# Verdict:
# Runtime: 1309 ms, faster than 12.12% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 28.8 MB, less than 33.79% of Python3 online submissions for Maximum Subarray.

# Solution 1: Brute force
class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        n = len(arr)
        maxSum = -1e8
        for i in range(0, n):
            currSum = 0
            for j in range(i, n):
                currSum = currSum + arr[j]
                if(currSum > maxSum):
                    maxSum = currSum
        return maxSum
      
# Verdict:
# TLE
