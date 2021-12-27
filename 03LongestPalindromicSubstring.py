# Question: https://leetcode.com/problems/longest-palindromic-substring/

# Solution 1: Dynamic Programming (N2 + N2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = 0
        length = 1
        # Declare a DP table
        dp = [[0 for x in range(n)] for y in range(n)]
        # Diagonal elements to be same (Length = 1)
        for i in range(n):
            dp[i][i] = 1
        # Elements of size = 2 
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                start = i
                length = 2
        # Elements of size = 3
        for k in range(3, n+1):
            for i in range(0, n-k+1):
                j = i+k-1
                if dp[i+1][j-1] == 1 and s[i] == s[j]:
                    dp[i][j] = 1
                    if k > length:
                        length = k
                        start = i
        return s[start : start+length]
# Verdict:
# Runtime: 8824 ms, faster than 5.03% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 22.8 MB, less than 6.11% of Python3 online submissions for Longest Palindromic Substring.

# Solution 2: Expand around the center (N2 + 1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # Get palindrome from left to right inclusively, index grows from center to outer
        def central_expand(self, left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left = left - 1
                right = right + 1
            return s[left+1 : right]
        ans = ""
        for i in range(n):
            # Odd length pattern s -> asa
            odd_expand = central_expand(s, i, i)
            if len(odd_expand) > len(ans):
                ans = odd_expand
            # Even le
            even_expand = central_expand(s, i, i+1)
            if len(even_expand) > len(ans):
                ans = even_expand
        return ans
# Verdict:
# Runtime: 836 ms, faster than 87.48% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 14.4 MB, less than 35.61% of Python3 online submissions for Longest Palindromic Substring.
