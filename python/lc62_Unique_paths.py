class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = {} # (row, col): unique paths
        
        def paths(row, col):
            if (row, col) in mem:
                return mem[(row, col)]
            
            if row == 0 or col == 0:
                return 1
            
            mem[(row, col)] = paths(row - 1, col) + paths(row, col - 1)
            
            return mem[(row, col)]
        
        return paths(m - 1, n - 1)

class Recursive_mem:
    def __init__(self):
        self.mem = {}
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        
        if (m,n) in self.mem:
            return self.mem[(m,n)]
        
        self.mem[(m,n)] = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        return self.mem[(m,n)]

class DP_BottomUp:
    """
    Time: O(M*N)
    Space: O(M*N)
    """
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n for _ in range(m)]
            
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m - 1][n - 1]

if __name__ == "__main__":
    m = 3
    n = 7
    S = DP()
    print(S.uniquePaths(m, n))  # 28