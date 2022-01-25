# Question: https://leetcode.com/problems/decode-ways/

# Generalization:
'''
Case 1: number of i and i-1 between 10 and 26:
        ways[i] = ways[i-1] + ways[i-2]
Case 2: number of i and i-1 larger than 26:
        ways[i] = ways[i-1]
Case 3: number of i==0 and i-1 == 1 or i-1 == 2:
        ways[i] = ways[i-2]
Case 4: number of i == 0 and i-1>2:
        stop and return 0
'''    

# ------------------------------------------------------------------------------------------------- #

# Solution 3: Dynamic Programming O(N)+O(N)
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*(len(s)+1)
        dp[0] = 1
        if s[0] == '0':
            return 0
        else:
            dp[1] = 1
        for i in range(2, len(s)+1):
            if s[i-1] == '0':
                if s[i-2] == '1' or s[i-2] == '2':
                    dp[i] = dp[i-2]
                else:
                    return 0
            else:
                if (s[i-2] == '1') or (s[i-2] == '2' and int(s[i-1]) < 7):
                    dp[i] = dp[i-2] + dp[i-1]
                else:
                    dp[i] += dp[i-1]
        return dp[len(s)]
      
# Verdict:
# Runtime: 54 ms, faster than 20.20% of Python3 online submissions for Decode Ways.
# Memory Usage: 14.1 MB, less than 95.33% of Python3 online submissions for Decode Ways.

# ------------------------------------------------------------------------------------------------- #

# Solution 2: Recursion + Memoization O(N) + O(N)
class Solution:
    def numDecodings(self, s: str) -> int:
        def backtrack(curr, code, memo):
            if curr == 0:
                if code[curr] == '0':
                    memo[curr] = 0
                    return 0
                else:
                    memo[curr] = 1
                    return 1
            if curr == -1:
                return 1
            if memo[curr] != -1:
                return memo[curr]
            if code[curr] == '0':
                if code[curr-1] == '1' or code[curr-1] == '2':
                    memo[curr] = backtrack(curr-2, code, memo)
                    return memo[curr]
                else:
                    memo[curr] = 0
                    return memo[curr]
            ways = 0
            if (code[curr-1] == '1') or (code[curr-1] == '2' and int(code[curr]) < 7):
                ways = backtrack(curr-1, code, memo) + backtrack(curr-2, code, memo)
            else:
                ways = backtrack(curr-1, code, memo)
            memo[curr] = ways
            return ways
        memo = [-1 for i in range(len(s))]
        return backtrack(len(s)-1, s, memo)

# Verdict:
# Runtime: 49 ms, faster than 28.12% of Python3 online submissions for Decode Ways.
# Memory Usage: 14.2 MB, less than 85.91% of Python3 online submissions for Decode Ways.

# ------------------------------------------------------------------------------------------------- #

# Solution 1: Brute Force: Backtracking all possibilities O(2^N) + O(N)
class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache
        def backtrack(curr, code):
            if curr == 0:
                if code[curr] == '0':
                    return 0
                else:
                    return 1
            if curr == -1:
                return 1
            if code[curr] == '0':
                if code[curr-1] == '1' or code[curr-1] == '2':
                    return backtrack(curr-2, code)
                else:
                    return 0
            ways = 0
            if (code[curr-1] == '1') or (code[curr-1] == '2' and int(code[curr]) < 7):
                ways = backtrack(curr-1, code) + backtrack(curr-2, code)
            else:
                ways = backtrack(curr-1, code)
            return ways
        return backtrack(len(s)-1, s)

# Verdict:
# Runtime: 70 ms, faster than 5.19% of Python3 online submissions for Decode Ways.
# Memory Usage: 14.5 MB, less than 17.96% of Python3 online submissions for Decode Ways.

# ------------------------------------------------------------------------------------------------- #
