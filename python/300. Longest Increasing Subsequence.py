"""
2021.4
idea:
1. DP
  - dp status is the length of largest increasing subsequence, dp[i] means the first ith status
  - transfer equation is that dp[i] = max(dp[i], dp[j]+1) when nums[i] > nums[j]
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
