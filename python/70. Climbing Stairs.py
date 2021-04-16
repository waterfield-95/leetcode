"""
2021.4
idea: DP, recursive
1. DP
  - state transition equation: dp[n] = dp[n-1] + dp[n-2]
  - boundary: dp[1]=1, dp[2]=2
  - validation: dp[3], d[4], dp[5] satisfied above condition
2. recursive
  - similar with DP (Essentially the same)
  - same with Fibonacci sequence
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            first = 1
            second = 2
            for i in range(3, n+1):
                first, second = second, first+second
            return second

    def climbStairs2(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs2(n-1) + self.climbStairs2(n-2)


if __name__ == '__main__':
    n = 5
    S = Solution()
    print(S.climbStairs2(n))
