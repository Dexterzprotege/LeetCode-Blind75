# Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# ----------------------------------------------------------------------------------------------------------- #

# Solution 3: Cleaner way, but same as solution 2
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            currentProfit = prices[i] - minPrice
            minPrice = min(minPrice, prices[i])
            maxProfit = max(maxProfit, currentProfit)
        return maxProfit

# Verdict
# Runtime: 1128 ms, faster than 57.94% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25 MB, less than 81.39% of Python3 online submissions for Best Time to Buy and Sell Stock.

# ----------------------------------------------------------------------------------------------------------- #

# Solution 2: Two pointer: Fix the local minima
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        ans = 0
        n = len(prices)
        while right < n:
            if prices[left] > prices[right]:
                left = right
            else:
                ans = max(ans, prices[right]-prices[left])
            right += 1
        return ans

# Verdict:
# Runtime: 1686 ms, faster than 21.36% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 24.9 MB, less than 97.83% of Python3 online submissions for Best Time to Buy and Sell Stock.

# ----------------------------------------------------------------------------------------------------------- #

# Solution 1: Brute Force:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                ans = max(ans, prices[j]-prices[i])
        return ans
      
# Verdict
TLE

# ----------------------------------------------------------------------------------------------------------- #
