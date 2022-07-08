# Question: https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def dfs(node):
            if not node:
                return 0
    
            # Compute left max and right max sum of subtrees
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            leftMax, rightMax = max(0, leftMax), max(0, rightMax)
            
            # Compute max path with split
            res[0] = max(res[0], node.val + leftMax + rightMax)
            
            # Compute max path considering any one of subtree
            return node.val + max(leftMax, rightMax)
        dfs(root)
        return res[0]
      
# Verdict:
# Runtime: 135 ms, faster than 47.14% of Python3 online submissions for Binary Tree Maximum Path Sum.
# Memory Usage: 21.4 MB, less than 61.77% of Python3 online submissions for Binary Tree Maximum Path Sum.
