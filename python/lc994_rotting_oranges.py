from typing import List
import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        minites = 0
        
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i, j])
        
        k = len(q)
        
        while q:
            if k == 0:
                # we finish one round of processing
                k = len(q)
                minites += 1
            
            row, col = q.popleft()
            k -= 1
            
            if row - 1 >= 0 and grid[row - 1][col] == 1:
                grid[row - 1][col] = 2
                q.append([row - 1, col])
            if row + 1 < m and grid[row + 1][col] == 1:
                grid[row + 1][col] = 2
                q.append([row + 1, col])
            if col - 1 >= 0 and grid[row][col - 1] == 1:
                grid[row][col - 1] = 2
                q.append([row, col - 1])
            if col + 1 < n and grid[row][col + 1] == 1:
                grid[row][col + 1] = 2
                q.append([row, col + 1])
                
        print(grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return minites
        
        