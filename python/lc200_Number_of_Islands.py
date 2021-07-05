"""
2021.7.5
idea: given grid with '1' island and '0' water, return the number of island
1. DFS: traverse each cell and set the visited as water '0'
    - count traversal times
    - DFS just for traverse all cells
    - Time complexity: O(MN), double layer traverse
    - Space complexity: O(MN) -> the maximum recusive depth
"""

from typing import List
from utils.functin_timer import func_timer

class Solution:
    def dfs(self, grid, r, c):
        nr = len(grid)
        nc = len(grid[0])
        grid[r][c] = '0'
        if r-1>=0 and grid[r-1][c] == '1': self.dfs(grid, r-1, c)
        if r+1<nr and grid[r+1][c] == '1': self.dfs(grid, r+1, c)
        if c-1>=0 and grid[r][c-1] == '1': self.dfs(grid, r, c-1)
        if c+1<nc and grid[r][c+1] == '1': self.dfs(grid, r, c+1)
        return


    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if not nr: return 0
        nc = len(grid[0])
        nums_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    nums_islands += 1
                    self.dfs(grid, r, c)
        return nums_islands

# DFS 2021.7
class SolutionDFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        # n_row, n_column  are larger than 0
        n_row, n_column = len(grid), len(grid[0])
        
        def dfs(i,j):
            """
            dfs to traverse one island and set '1' to '0'
            """
            nonlocal grid, n_row, n_column
            grid[i][j] = '0'
            if i-1>=0 and grid[i-1][j] == '1': dfs(i-1, j)
            if i+1<n_row and grid[i+1][j] == '1': dfs(i+1, j)
            if j-1>=0 and grid[i][j-1] == '1': dfs(i, j-1)
            if j+1<n_column and grid[i][j+1] == '1': dfs(i, j+1)
            return
        
        num = 0
        for row in range(n_row):
            for column in range(n_column):
                if grid[row][column] == '1':
                    num += 1
                    dfs(row, column)

        return num


# Notice: 
class SolutionBFS:
    @func_timer
    def numIslands(self, grid: List[List[str]]) -> int:
        n_row, n_column = len(grid), len(grid[0])
        
        from collections import deque
        queue_ = deque()

        num = 0
        for i in range(n_row):
            for j in range(n_column):
                if grid[i][j] == '1':
                    num += 1
                    grid[i][j] = '0'
                    queue_.append((i, j))
                    while queue_:
                        row, column = queue_.popleft()
                        # Limited Time Exceeded (don't know why?)
                        # grid[row][column] = '0'   
                        for x,y in [(row-1, column), (row+1, column), (row, column-1), (row, column+1)]:
                            if 0<=x<n_row and 0<=y<n_column and grid[x][y] == '1':
                                queue_.append((x,y))
                                grid[x][y] = '0'
        return num


if __name__ == '__main__':
    grid = [["1","0","0","1","1","1","0","1","1","0","0","0","0","0","0","0","0","0","0","0"],["1","0","0","1","1","0","0","1","0","0","0","1","0","1","0","1","0","0","1","0"],["0","0","0","1","1","1","1","0","1","0","1","1","0","0","0","0","1","0","1","0"],["0","0","0","1","1","0","0","1","0","0","0","1","1","1","0","0","1","0","0","1"],["0","0","0","0","0","0","0","1","1","1","0","0","0","0","0","0","0","0","0","0"],["1","0","0","0","0","1","0","1","0","1","1","0","0","0","0","0","0","1","0","1"],["0","0","0","1","0","0","0","1","0","1","0","1","0","1","0","1","0","1","0","1"],["0","0","0","1","0","1","0","0","1","1","0","1","0","1","1","0","1","1","1","0"],["0","0","0","0","1","0","0","1","1","0","0","0","0","1","0","0","0","1","0","1"],["0","0","1","0","0","1","0","0","0","0","0","1","0","0","1","0","0","0","1","0"],["1","0","0","1","0","0","0","0","0","0","0","1","0","0","1","0","1","0","1","0"],["0","1","0","0","0","1","0","1","0","1","1","0","1","1","1","0","1","1","0","0"],["1","1","0","1","0","0","0","0","1","0","0","0","0","0","0","1","0","0","0","1"],["0","1","0","0","1","1","1","0","0","0","1","1","1","1","1","0","1","0","0","0"],["0","0","1","1","1","0","0","0","1","1","0","0","0","1","0","1","0","0","0","0"],["1","0","0","1","0","1","0","0","0","0","1","0","0","0","1","0","1","0","1","1"],["1","0","1","0","0","0","0","0","0","1","0","0","0","1","0","1","0","0","0","0"],["0","1","1","0","0","0","1","1","1","0","1","0","1","0","1","1","1","1","0","0"],["0","1","0","0","0","0","1","1","0","0","1","0","1","0","0","1","0","0","1","1"],["0","0","0","0","0","0","1","1","1","1","0","1","0","0","0","1","1","0","0","0"]]
    S = SolutionBFS()
    print(S.numIslands(grid))