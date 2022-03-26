from typing import List

class Optimal:
    """
    T: O(nm)
    Space: O(1)
    - Use first row and column to record if this row or column should be zeroes
    - For the first row, we use cell[0][0] and for first column, use col_zero
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        first_col_zero = False
        
        for i in range(n):
            if matrix[i][0] == 0:
                first_col_zero = True
            # matrix[0][0] would mark for first row
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0
                
        if first_col_zero:
            for i in range(n):
                matrix[i][0] = 0

        
        return matrix

class Solution:
    """
    Time: O(mn)
    Space: O(m+n)
    Records distinct rows and columns which need to be set to zeroes
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        row_set = set()
        column_set = set()
        n = len(matrix)
        m = len(matrix[0])
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    column_set.add(j)
                    
        for row in list(row_set):
            for j in range(m):
                matrix[row][j] = 0
                
        for column in list(column_set):
            for i in range(n):
                matrix[i][column] = 0
        
        return matrix