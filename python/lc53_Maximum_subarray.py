"""
2021.7
same as : lcof42_max_sum_of_continuous_subarray

Given num array, return the max sum of continuous subarray. (The same as lc53)
- Dynamic Programming: dp[i] -> the max sum in the end of nums[i]
    - dp[i] = max(dp[i-1]+nums[i], nums[i])
    - scrolling: 
"""

from typing import List

class Solution:
    """
    state transition in the original array without extra space
    """
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)

class DP1:
    """
    original dp, dp[i] is the max sum in the subarray which is end of nums[i]
    """
    def maxSubArray(self, nums):
        n = len(nums)
        dp = [0] * n
        for i in range(1, n):
            dp[i] = max(dp[i-1]+nums[i-1], nums[i-1])
        return max(dp)
        

class Scrolling:
    """
    scrolling array without array, using two variable: first, second
    """
    def maxSubArray(self, nums):
        dp = nums[0]   # to record current max sum of subarray including the current element
        max_ = nums[0]    # the max sum
        for i in range(1, len(nums)):
            dp = max(dp + nums[i], nums[i])
            max_ = max(max_, dp)
        return max_


if __name__ == '__main__':
    nums_ = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    S = Solution()
    S1 = DP1()
    S2 = Scrolling()
    # print(S.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))   # modify nums in space
    # print(S1.maxSubArray(nums_))
    print(S2.maxSubArray(nums_))

