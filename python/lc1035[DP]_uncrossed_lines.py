"""
2021.5
idea: 2-dimensional Dynamic Programming
    - Similar with lc1143: Longest Common Subsequence
    - set extra 0 rows and columns as base case
    - dynamic states equation
"""


from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        dp = [[0] * (n2+1) for _ in range(n1+1)]
        for i in range(n1):
            for j in range(n2):
                if nums1[i] == nums2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return dp[n1][n2]


if __name__ == '__main__':
    nums1 = [1,4,2]
    nums2 = [1,2,4]
    S = Solution()
    print(S.maxUncrossedLines(nums1, nums2))