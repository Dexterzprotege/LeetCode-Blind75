# Question: https://leetcode.com/problems/3sum/

# Solution:
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Return null if array length is less than 3
        if len(nums) < 3: return []
        n = len(nums)
        result = []
        nums = sorted(nums)
        
        for i in range(0, n-2):
            # Duplicate elements continue
            if i>0 and nums[i]==nums[i-1]:
                continue
            # Fix three pointers: i, left and right which are variable
            left = i + 1
            right = n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                # If sum is 0 add result to the ans
                if s == 0:
                    temp = []
                    temp.append(nums[i])
                    temp.append(nums[left])
                    temp.append(nums[right])
                    result.append(temp)
                    
                    left += 1
                    right -= 1
                    
                    # Checking for the duplicates of left
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                    # Checking for the duplicates of right
                    while nums[right] == nums[right+1] and left < right:
                        right -= 1
                elif s > 0:
                    right -= 1
                else:
                    left += 1
        return result
 
# Verdict:
# Runtime: 908 ms, faster than 62.66% of Python3 online submissions for 3Sum.
# Memory Usage: 17.6 MB, less than 49.54% of Python3 online submissions for 3Sum.
