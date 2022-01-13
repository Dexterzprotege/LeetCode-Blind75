# Question: https://leetcode.com/problems/unique-paths/

# Solution 5: Combinatrics Math O(1) + O(1)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total_movements = n + m - 2 # Need to do n + m - 2 movements : m - 1 down, n - 1 right, because we start from cell (1, 1).
        steps_to_go_down = m - 1 # number of steps that need to go down
        result = 1
        # here we calculate the total possible path number 
        # Combination(N, k) = n! / (k!(n - k)!)
        # reduce the numerator and denominator and get
        # C = ( (n - k + 1) * (n - k + 2) * ... * n ) / k!
        for i in range(1, steps_to_go_down+1):
            result = result * (total_movements - steps_to_go_down + i) / i
        return int(result)
    
    from math import comb
    def uniquePaths(self, m: int, n: int) -> int:
        total_movements = n + m - 2 # Need to do n + m - 2 movements : m - 1 down, n - 1 right, because we start from cell (1, 1).
        steps_to_go_down = m - 1 # number of steps that need to go down
        return comb(total_movements, steps_to_go_down)

# Verdict:
# Runtime: 51 ms, faster than 11.38% of Python3 online submissions for Unique Paths.
# Memory Usage: 14 MB, less than 96.24% of Python3 online submissions for Unique Paths.

# ------------------------------------------------------------------------------------------------------ #
# Solution 4: Dynamic Programming Space Optimised O(MN) + O(N)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]*n
        for i in range(m-1):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[-1]

# Verdict:
# Runtime: 38 ms, faster than 24.13% of Python3 online submissions for Unique Paths.
# Memory Usage: 14.2 MB, less than 86.71% of Python3 online submissions for Unique Paths.

# ------------------------------------------------------------------------------------------------------ #
# Solution 3: Dynamic Programming O(NM) + O(NM)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n] * m
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

# Verdict:
# Runtime: 47 ms, faster than 15.13% of Python3 online submissions for Unique Paths.
# Memory Usage: 14.3 MB, less than 38.56% of Python3 online submissions for Unique Paths.

# ------------------------------------------------------------------------------------------------------ #
# Solution 2: Recursive + Memoization 
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        
        def recursion(m, n):
            if (m, n) in memo:
                return memo[(m, n)]
            if m == 0 or n == 0:
                memo[(m, n)] = 0
                return 0
            elif m == 1 and n == 1:
                memo[(m, n)] = 1
                return 1
            memo[(m, n)] = recursion(m-1, n) + recursion(m, n-1)
            
            return memo[(m, n)]
        
        return recursion(m, n)

# Verdict:
# Runtime: 58 ms, faster than 6.04% of Python3 online submissions for Unique Paths.
# Memory Usage: 14.7 MB, less than 6.23% of Python3 online submissions for Unique Paths.

# ------------------------------------------------------------------------------------------------------ #
# Solution 1: Recursion Exponential solution
class Solution:
    def uniquePaths(self, m: int, n: int, i = 0, j = 0) -> int:
        if i == m-1 and j == n-1:
            return 1
        if i >= m or j >= n:
            return 0
        return self.uniquePaths(m, n, i+1, j) + self.uniquePaths(m, n, i, j+1)

# Verdict:
# TLE
# ------------------------------------------------------------------------------------------------------ #
