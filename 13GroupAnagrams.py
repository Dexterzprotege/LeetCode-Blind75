# Question: https://leetcode.com/problems/group-anagrams/

# Solution:
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in sorted(strs):
            key = ''.join(sorted(word))
            if key in dic:
                dic.get(key).append(word)
            else:
                dic[key] = [word]
        
        return dic.values()

# Verdict:
# Runtime: 159 ms, faster than 16.79% of Python3 online submissions for Group Anagrams.
# Memory Usage: 17.5 MB, less than 67.02% of Python3 online submissions for Group Anagrams.
