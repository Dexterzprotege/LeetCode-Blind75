# Question:

# Solution 1: Brute Force + Backtracking
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(board, i, j, word, index):
            # If we reach the word length return True
            if len(word) <= index:
                return True
            # If off-bounds return 
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j]=='*' or board[i][j]!=word[index]:
                return False
             
            # Setting the seen node so that we dont visit again
            temp = board[i][j]
            board[i][j] = '*'
            
            # Recursion on all 4 sides of the board
            if backtrack(board, i-1, j, word, index+1) or backtrack(board, i, j-1, word, index+1) or backtrack(board, i+1, j, word, index+1) or backtrack(board, i, j+1, word, index+1):
                return True
            
            # False scenario: Setting the node to be unseen
            board[i][j] = temp
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtrack(board, i, j, word, 0):
                        return True
        return False

# Verdict:
# Runtime: 7738 ms, faster than 31.94% of Python3 online submissions for Word Search.
# Memory Usage: 14.3 MB, less than 46.75% of Python3 online submissions for Word Search.
