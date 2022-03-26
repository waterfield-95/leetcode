"""
2021.4 
idea: 2-dimensional dynamic programming
  - set web table with a extra row and column which is filled with 0
  - cell[i][j] represents the largest common sequence between text1[0:i] and text2[0:j]
  - boundary: cell[0][j] and cell[i][0] are equal to 0
  - dp transfer equation:
    - when text1[i-1] is equal to text2[j-1], cell[i][j] = cell[i-1][j-1] + 1
    - otherwise, cell[i][j] = max(cell[i-1][j], cell[i][j-1])
"""


class DP:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        # n*m matrix, record longest common subsequence based on text1[0-i], text2[0-j]
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[n][m]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0 for i in range(m+1)] for i in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]

    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0 for i in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1
                else:
                    if i==0 and j!=0:
                        dp[i][j] = dp[i][j-1]
                    elif i != 0 and j == 0:
                        dp[i][j] = dp[i-1][j]
                    elif i == 0 and j == 0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n-1][m-1]


if __name__ == '__main__':
    text1 = 'abcde'
    text2 = 'ace'
    S = Solution()
    print(S.longestCommonSubsequence2(text1, text2))
