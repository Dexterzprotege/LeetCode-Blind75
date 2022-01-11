# Question: https://leetcode.com/problems/insert-interval/

# Solution2: In place O(N):
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        for interval in intervals:
            if interval[0] > newInterval[1]:
                ans.append(newInterval)
                newInterval = interval
            elif interval[1] >= newInterval[0]:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
            else:
                ans.append(interval)
        ans.append(newInterval)
        return ans

# Verdict:
# Runtime: 198 ms, faster than 5.07% of Python3 online submissions for Insert Interval.
# Memory Usage: 17.5 MB, less than 32.63% of Python3 online submissions for Insert Interval.

# Solution1: Insert and then use mergeLists: O(NLogN) + O(N)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def mergeIntervals(intervals):
            intervals = sorted(intervals)
            ans = []
            print(intervals)
            for interval in intervals:
                if not ans or ans[-1][1] < interval[0]:
                    ans.append(interval)
                else:
                    ans[-1][1] = max(ans[-1][1], interval[1])
            return ans
        
        intervals.append(newInterval)
        return mergeIntervals(intervals)

# Verdict:
# Runtime: 127 ms, faster than 15.73% of Python3 online submissions for Insert Interval.
# Memory Usage: 17.6 MB, less than 32.63% of Python3 online submissions for Insert Interval.
