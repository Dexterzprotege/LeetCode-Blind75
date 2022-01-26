# Question: https://leetcode.com/problems/validate-binary-search-tree/

# Similar can be applied to - InOrder, KthSmallest, Validate

# -------------------------------------------------------------------------------------- #

# Solution 2: Iteratve Stack
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        stack = []
        pre = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre and root.val <= pre.val:
                return False
            pre = root
            root = root.right
        return True
      
# Verdict:
# Runtime: 44 ms, faster than 81.53% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16.4 MB, less than 53.91% of Python3 online submissions for Validate Binary Search Tree.

# -------------------------------------------------------------------------------------- #

# Solution 1: Recursive InOrder
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], minn = float('-inf'), maxx = float('inf')) -> bool:
        if root is None:
            return True
        if root.val <= minn or root.val >= maxx:
            return False
        return self.isValidBST(root.left, minn, root.val) and self.isValidBST(root.right, root.val, maxx)
      
# Verdict:
# Runtime: 84 ms, faster than 10.46% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16.4 MB, less than 53.91% of Python3 online submissions for Validate Binary Search Tree.

# -------------------------------------------------------------------------------------- #
