# Question: https://leetcode.com/problems/container-with-most-water/

# Solution:
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Function to calculate area: Minimum height, max width
        def getArea(self, left, right):
            x = abs(right-left)
            y = min(height[left], height[right])
            return x*y
        
        n = len(height)
        left, right = 0, n-1
        area = 0
        while left < right:
            area = max(area, getArea(height, left, right))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return area

# Verdict:
# Runtime: 740 ms, faster than 66.18% of Python3 online submissions for Container With Most Water.
# Memory Usage: 27.6 MB, less than 22.10% of Python3 online submissions for Container With Most Water.
