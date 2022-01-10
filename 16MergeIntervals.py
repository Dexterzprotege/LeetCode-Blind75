# Question: https://leetcode.com/problems/merge-intervals/

# Solution:
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        ans = []
        print(intervals)
        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans
      
# Verdict:
# Runtime: 186 ms, faster than 12.69% of Python3 online submissions for Merge Intervals.
# Memory Usage: 18.2 MB, less than 7.15% of Python3 online submissions for Merge Intervals.
