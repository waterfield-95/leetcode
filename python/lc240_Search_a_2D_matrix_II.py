from typing import List

class Optimal:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        # cache these, as they won't change
        height = len(matrix)
        width = len(matrix[0])
        
        # start pointer in the bottom-left
        row = height - 1 
        column = 0
        
        while column < width and row >= 0:
            if matrix[row][column] == target:
                return True
            else:
                if matrix[row][column] > target:
                    row -= 1
                else:
                    column += 1
        
        return False
    
    # Time: O(n+m)
    # Space: O(1)
        

class Solution:
    """
    Time: O(x^(0.5)logx^(0.5)), x=n^2 nlog(n), n=n*m (m ~=n)
    Space: O(logN)
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # an empty matrix obviously does not contain target
        if not matrix:
            return False
        
        def search_rec(left, up, right, down):
            # this submatrix has no height or no width
            if left > right or up > down:
                return False
            
            # target is already larger than the largest element or smaller than the smallest element in the submatrix
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False
            
            mid = left + (right-left) //2
            
            # locate the row such that matrix[row-1][mid] < target < matrix[row][mid]
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            
            return search_rec(left, row, mid-1, down) or search_rec(mid+1, up, right, row-1)

        return search_rec(0, 0, len(matrix[0]) - 1, len(matrix) - 1)


