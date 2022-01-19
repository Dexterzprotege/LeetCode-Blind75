# Question: https://leetcode.com/problems/minimum-window-substring/

# Solution:
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = {}
        s_dict = {}
        for i in t:
            if i not in t_dict: t_dict[i] = 1
            else:   t_dict[i] += 1
        left = right = count = 0
        n = len(s)
        minimum = float('inf')
        min_str = ""
        while right < n:
            ch = s[right]
            if ch not in s_dict:    s_dict[ch] = 1
            else:   s_dict[ch] += 1
            if ch in t_dict:
                if s_dict[ch] <= t_dict[ch]:
                    count += 1
            while left <= right and count == len(t):
                if minimum > right - left + 1:
                    minimum = right - left + 1
                    min_str = s[left: right+1]
                
                s_dict[s[left]] -= 1
                if s[left] in t_dict and s_dict[s[left]] < t_dict[s[left]]:
                    count-=1
                left += 1
            right += 1
        return min_str

# Verdict:
# Runtime: 121 ms, faster than 58.37% of Python3 online submissions for Minimum Window Substring.
# Memory Usage: 14.9 MB, less than 28.41% of Python3 online submissions for Minimum Window Substring.
