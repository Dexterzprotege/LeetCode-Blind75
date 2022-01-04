# Question: https://leetcode.com/problems/rotate-image/

# Solution1: Transpose and rotate rows
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def transpose(arr):
            n = len(arr)
            for i in range(0, n):
                for j in range(i+1, n):
                    arr[j][i], arr[i][j] = arr[i][j], arr[j][i]
            return arr
        
        def reverse(arr):
            n = len(arr)
            for x in range(0, n):
                i = 0
                j = n-1
                while i < j:
                    arr[x][i], arr[x][j] = arr[x][j], arr[x][i]
                    i += 1
                    j -= 1
            return arr
        
        matrix = transpose(matrix)
        matrix = reverse(matrix)

# Verdict:
# Runtime: 44 ms, faster than 19.05% of Python3 online submissions for Rotate Image.
# Memory Usage: 14.3 MB, less than 30.52% of Python3 online submissions for Rotate Image.

# Solution2: Fixing the last 4 and rotation based on that
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        import math
        n = len(matrix)
        x = math.floor(n/ 2)
        y = n - 1
        for i in range(0,x):
            for j in range(i, y-i):
                k = matrix[i][j];
                matrix[i][j] = matrix[y - j][i]
                matrix[y - j][i] = matrix[y - i][y - j]
                matrix[y - i][y - j] = matrix[j][y - i]
                matrix[j][y - i] = k
         
# Verdict:
# Runtime: 62 ms, faster than 6.08% of Python3 online submissions for Rotate Image.
# Memory Usage: 14.3 MB, less than 60.91% of Python3 online submissions for Rotate Image.
