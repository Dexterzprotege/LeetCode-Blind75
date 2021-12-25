# Question: https://leetcode.com/problems/two-sum/

# Solution:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Declare an empty dictionary/map
        dic = {}
        for i in range(len(nums)):
            # calculate difference element
            temp = target-nums[i]
            # search whether the difference element is in the dictionary or not, this happens only once in the solution so return it
            if temp in dic:
                return [dic[temp], i]
            # else add the value to the map
            else:
                dic[nums[i]] = i
                
# Verdict:
# Runtime: 66 ms, faster than 52.34% of Python3 online submissions for Two Sum.
# Memory Usage: 15.4 MB, less than 40.36% of Python3 online submissions for Two Sum.
