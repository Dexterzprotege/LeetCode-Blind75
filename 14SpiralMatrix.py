# Question: https://leetcode.com/problems/spiral-matrix/

# Solution:
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        rowBegin, rowEnd, colBegin, colEnd = 0, len(matrix)-1, 0, len(matrix[0])-1
        
        while rowBegin <= rowEnd and colBegin <= colEnd:
            # Traverse Right
            for i in range(colBegin,colEnd+1):
                res.append(matrix[rowBegin][i])
            rowBegin += 1
            
            # Traverse Down
            for i in range(rowBegin,rowEnd+1):
                res.append(matrix[i][colEnd])
            colEnd -= 1
            
            # Traverse Left
            if (rowBegin <= rowEnd):
                for i in range(colEnd,colBegin-1,-1):
                    res.append(matrix[rowEnd][i])
                rowEnd -= 1
                
            # Traverse Right
            if (colBegin <= colEnd):
                for i in range(rowEnd,rowBegin-1,-1):
                    res.append(matrix[i][colBegin])
                colBegin += 1
            
        return res 

# Verdict:
# Runtime: 42 ms, faster than 20.11% of Python3 online submissions for Spiral Matrix.
# Memory Usage: 14.1 MB, less than 83.71% of Python3 online submissions for Spiral Matrix.
