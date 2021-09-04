from typing import List

class RotateGroups:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix[0]) - 1
        while left < right:
            top, bottom = left, right
            for i in range(right - left):
                tmp = matrix[top][left + i]
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = tmp
            left += 1
            right -= 1

class flipFlip:
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    
    def reflect(self, matrix):
        """
        flip from left to right
        """
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-1-j] = matrix[i][-1-j], matrix[i][j]                

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()    # in-place reverse list
        self.transpose(matrix)
        
        
if __name__ == '__main__':
    pass