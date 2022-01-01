# Question: https://leetcode.com/problems/search-in-rotated-sorted-array/

# Solution:
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left+right)//2
            
            # Fixing the Pivot position, before the change or after
            if (nums[mid] < nums[0]) == (target < nums[0]):
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid
                else:
                    return mid
            elif target < nums[0]:
                left = mid+1
            else:
                right = mid
        return -1

# Verdict:
# Runtime: 68 ms, faster than 6.56% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 14.6 MB, less than 55.90% of Python3 online submissions for Search in Rotated Sorted Array.
