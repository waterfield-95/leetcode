from typing import List

class NumMatrix:
    """
    self.aux[i][j] records the sum from (0,0) to (i,j)
    """
    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.aux = [[0 for _ in range(m)] for _ in range(n)]
        
        # initial
        self.aux[0][0] = matrix[0][0]
        for i in range(1, n):
            self.aux[i][0] = self.aux[i-1][0] + matrix[i][0]
        for j in range(1, m):
            self.aux[0][j] = self.aux[0][j-1] + matrix[0][j]
        
        for i in range(1, n):
            for j in range(1, m):
                self.aux[i][j] = matrix[i][j] + self.aux[i-1][j] + self.aux[i][j-1] - self.aux[i-1][j-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # assume: row2 >= row1, column2>=column1
        # case0: start point is (0,0)
        if row1 == 0 and col1 == 0:
            ans = self.aux[row2][col2]
        elif row1 == 0: # col1 != 0
            ans = self.aux[row2][col2] - self.aux[row2][col1-1]
        elif col1 == 0: # row1 != 0
            ans = self.aux[row2][col2] - self.aux[row1 - 1][col2]
        else: # Both are not equal to 0
            ans = self.aux[row2][col2] - self.aux[row1-1][col2] - self.aux[row2][col1-1] + self.aux[row1-1][col1-1]
        return ans

class NumMatrix2:
    """
    - make it easier by adding auxiliary row and column to aux array
    - self.aux[i+1][j+1] records the sum from (0,0) to (i,j)
    """
    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        # self.aux[i+1][j+1] records the sum from (0,0) to (i,j)
        self.aux = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                self.aux[i][j] = matrix[i-1][j-1] + self.aux[i-1][j] + self.aux[i][j-1] - self.aux[i-1][j-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.aux[row2+1][col2+1] - self.aux[row1][col2+1] - self.aux[row2+1][col1] + self.aux[row1][col1]
        return ans
        

if __name__ == "__main__":
    # matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    matrix = [[-4, -5]]
    row1, col1, row2, col2 = 0,1,0,1 #2,1,4,3
    S = NumMatrix(matrix)
    print(S.sumRegion(row1, col1, row2, col2))
