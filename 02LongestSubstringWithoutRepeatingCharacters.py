# Question: https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        dic = {}
        start = 0
        for end in range(0, n):
            key = s[end]
            # If a value is found in the map, it means it is repeating and we have to move the start and calculate the new start
            if key in dic:
                prev = dic[key]
                start = max(start, prev+1)
            dic[key] = end
            ans = max(ans, end-start+1)
        return ans
    
# Verdict:
# Runtime: 48 ms, faster than 96.26% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.4 MB, less than 55.00% of Python3 online submissions for Longest Substring Without Repeating Characters.
