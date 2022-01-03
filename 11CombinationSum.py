# Question:

# Solution:
class Solution:
    def backtrack(self, curr, target, index):
        if target == 0:
            self.combinations.append(curr)
            return 
        if target < 0:
            return 
        for i in range(index, len(self.candidates)):
            tmp = curr + [self.candidates[i]]
            self.backtrack(tmp, target-self.candidates[i], i)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.combinations = []
        self.candidates = sorted(candidates)
        self.backtrack([], target, 0)
        return self.combinations

# Verdict:
# Runtime: 184 ms, faster than 12.50% of Python3 online submissions for Combination Sum.
# Memory Usage: 14.3 MB, less than 78.03% of Python3 online submissions for Combination Sum.
