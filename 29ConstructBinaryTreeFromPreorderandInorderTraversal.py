# Question: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Terminal case
        if not preorder or not inorder:
            return None
        
        # Root is always the first element of Preorder traversal
        root = TreeNode(preorder[0])
        # Finding the index of root in Inorder so that left of it is left subtree and right of it is right subtree
        index = inorder.index(preorder[0])
        # Left Subtree
        # Preorder can be deduced from 1 (since 0 is root) to the index
        # Inorder can be deduced up to the index
        root.left = self.buildTree(preorder[1: index+1], inorder[ :index])
        # Right Subtree
        # Preorder and Inorder can be deduced to index to end as left is already done
        root.right = self.buildTree(preorder[index+1:], inorder[index+1: ])
        return root

# Verdict:
# Runtime: 337 ms, faster than 21.15% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
# Memory Usage: 88.6 MB, less than 40.68% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
