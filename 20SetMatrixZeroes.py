# Question: https://leetcode.com/problems/set-matrix-zeroes/

# ------------------------------------------------------------------------------------------------------------ #

# Solution 2: Inplace, using first row and first col as memory to keep track of zeroes O(N2) + O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        firstRow = firstCol = False
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    if i == 0:
                        firstRow = True
                    if j == 0:
                        firstCol = True
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, row):
            for j in range(1, col):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if firstRow:
            for j in range(col):
                matrix[0][j] = 0
        
        if firstCol:
            for i in range(row):
                matrix[i][0] = 0

# Verdict:
# Runtime: 132 ms, faster than 65.96% of Python3 online submissions for Set Matrix Zeroes.
# Memory Usage: 15.1 MB, less than 73.89% of Python3 online submissions for Set Matrix Zeroes.

# ------------------------------------------------------------------------------------------------------------ #

# Solution 1: Extra Space note the zero rows O(N2) + O(N)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = [], []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in cols:
                    matrix[i][j] = 0
                    
# Verdict:
# Runtime: 156 ms, faster than 37.96% of Python3 online submissions for Set Matrix Zeroes.
# Memory Usage: 15.3 MB, less than 13.82% of Python3 online submissions for Set Matrix Zeroes.
# ------------------------------------------------------------------------------------------------------------ #
