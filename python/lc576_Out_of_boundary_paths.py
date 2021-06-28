"""
2021.6
idea: Calculate the number of paths out of boundary given N step, initial location (i,j) and grid m*n
    - process: move 1 step in 4 directions(i/j +/- 1), and move next step (recursive -> DFS / DP)
    - base case: boundary status, i<0 or j<0 or i>=m or j>=n, if current step cross the boudary, result plus 1.
    If N is 0 and current status is still in the grid, keep result constant because there is no new route out of boundary
    - Variable: i, j, N
    - Bigint: result % int(1e9+7)

1. DFS with memorization 
2. DP
(DFS and DP are reciprocal process)
"""

from functools import lru_cache

# dfs with least-recently-used cache: AC
class Solution_1:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(None)
        def dfs(m, n, N, i, j):
            if (i<0 or j<0 or i>=m or j>=n):
                return 1
            if N == 0:
                return 0    # after N step, status is still in range
            res = 0
            dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            for dir in dirs:
                n_i = i + dir[0]
                n_j = j + dir[1]
                res = (res + dfs(m, n, N-1, n_i, n_j)) % int(1e9+7)
            return res
        
        return dfs(m, n, maxMove, startRow, startColumn)

# DFS with memorization: AC
class Solution_2:
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        MOD = int(1e9 + 7)
        memo = [[[-1] * (maxMove+1) for _ in range(n+1)] for _ in range(m+1)]
        def dfs(m, n, N, i, j):
            if i<0 or j<0 or i>=m or j>=n:
                return 1
            if N == 0:
                return 0
            if memo[i][j][N] != -1:
                return memo[i][j][N]

            res = 0
            directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            for dir in directions:
                n_i = i + dir[0]
                n_j = j + dir[1]
                res = (res + dfs(m, n, N-1, n_i, n_j)) % MOD

            memo[i][j][N] = res
            return res
        return dfs(m, n, maxMove, startRow, startColumn)

# DP: AC
class Solution_3:
    def findPaths(self, m, n, N, i, j):
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        dp = [[[0] * (N+1) for _ in range(n+1)] for _ in range(m+1)]
        res = 0
        dp[i][j][0] = 1
        for k in range(1, N+1):
            for i in range(0, m):
                for j in range(0, n):
                    for dir in dirs:
                        n_i = i + dir[0]
                        n_j = j + dir[1]
                        if n_i<0 or n_j<0 or n_i>=m or n_j>=n:
                            res = res + dp[i][j][k-1]
                        else:
                            dp[n_i][n_j][k] = dp[n_i][n_j][k] + dp[i][j][k-1]
        return res % int(1e9+7)

class Solution_4:
    @lru_cache(None)  #通过修饰器实现记忆化
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        count = 0
        if N < 0:
            return count
        if i < 0 or i >= m or j < 0 or j >= n:
            return 1
        for di, dj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            count = (count + self.findPaths(m, n, N-1, di, dj)) % 1000000007
        return count

class Solution_5:
    def findPaths(self, m, n, N, i, j):
        dp = [[[0]*(n+2) for _ in range(m+2)] for _ in range(N+1)]
        if N == 0:
            return 0
        for k in range(N+1):
            for x in range(m+2):
                for y in range(n+2):
                    if x == 0 or y == 0 or x==m+1 or y==n+1:     # equal to DFS base-case
                        dp[k][x][y] = 1
                    else:
                        if k == 0:
                            continue
                        else:
                            dp[k][x][y] = (dp[k][x][y] + dp[k-1][x-1][y] + dp[k-1][x][y-1] + dp[k-1][x+1][y] + dp[k-1][x][y+1]) % int(1e9+7)
        return dp[N][i+1][j+1]

if __name__ == '__main__':
    m, n = 2, 2
    maxMove = 2
    startRow, startColumn = 0, 0
    S = Solution()
    print(S.findPaths(m, n, maxMove, startRow, startColumn))
