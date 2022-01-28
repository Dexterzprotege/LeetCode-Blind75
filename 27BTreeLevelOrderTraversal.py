# Question: https://leetcode.com/problems/binary-tree-level-order-traversal/

# Solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        stack = [root]
        while root and stack:
            res.append([node.val for node in stack])
            temp = []
            for node in stack :
                if node.left!=None:
                    temp.append(node.left)
                if node.right!=None:
                    temp.append(node.right)
            stack = temp
        return res

# Verdict:
# Runtime: 50 ms, faster than 33.25% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 14.2 MB, less than 99.41% of Python3 online submissions for Binary Tree Level Order Traversal.
