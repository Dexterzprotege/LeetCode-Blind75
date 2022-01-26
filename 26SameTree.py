# Question: https://leetcode.com/problems/same-tree/

# ------------------------------------------------------------------------------------------ #

# Solution 2: Iterative
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p,q)]
        while stack :
            x,y = stack.pop()
            if x == None and y == None:
                continue
            if x == None or y == None:
                return False
            if x.val == y.val:
                stack.append((x.left,y.left))
                stack.append((x.right,y.right))
            else:
                return False
        return True     
      
# Verdict:
# Runtime: 47 ms, faster than 25.48% of Python3 online submissions for Same Tree.
# Memory Usage: 14.1 MB, less than 95.73% of Python3 online submissions for Same Tree.

# ------------------------------------------------------------------------------------------ #

# Solution 1: Recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Verdict:
# Runtime: 56 ms, faster than 11.06% of Python3 online submissions for Same Tree.
# Memory Usage: 14.2 MB, less than 62.62% of Python3 online submissions for Same Tree.

# ------------------------------------------------------------------------------------------ #
