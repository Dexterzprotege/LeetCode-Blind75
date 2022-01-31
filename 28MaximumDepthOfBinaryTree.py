# Question: https://leetcode.com/problems/maximum-depth-of-binary-tree/

# ----------------------------------------------------------------------------------------------------------- #

# Solution 2: Breadth-First solution, iteratvie
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        res=[]
        s=[root]
        while root and s:
            res.append([n.val for n in s])
            l=[]
            for n in s :
                if n.left!=None:
                    l.append(n.left)
                if n.right!=None:
                    l.append(n.right)
            s=l
        return len(res)

# Verdict
# Runtime: 75 ms, faster than 12.64% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 15.3 MB, less than 88.16% of Python3 online submissions for Maximum Depth of Binary Tree.

# ----------------------------------------------------------------------------------------------------------- #

# Solution 1: Depth-First solution, recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))

# Verdict
# Runtime: 85 ms, faster than 5.52% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 16.4 MB, less than 15.50% of Python3 online submissions for Maximum Depth of Binary Tree.

# ----------------------------------------------------------------------------------------------------------- #
