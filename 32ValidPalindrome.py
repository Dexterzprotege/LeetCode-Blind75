# Question: https://leetcode.com/problems/valid-palindrome/

# ----------------------------------------------------------------------------------------------------------- #

# Solution 2: Two pointer
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n-1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True

# Verdict
# Runtime: 48 ms, faster than 76.89% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 14.4 MB, less than 92.36% of Python3 online submissions for Valid Palindrome.

# ----------------------------------------------------------------------------------------------------------- #

# Solution 1: Pythonic
class Solution:
    def isPalindrome(self, s: str) -> bool:
        actual = ""
        for c in s:
            if c.isalnum():
                actual += c.lower()
        return actual == actual[::-1]

# Verdict:
# Runtime: 82 ms, faster than 22.80% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 14.4 MB, less than 92.36% of Python3 online submissions for Valid Palindrome.

# ----------------------------------------------------------------------------------------------------------- #
