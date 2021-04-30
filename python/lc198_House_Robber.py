"""
2021.4
idea: dynamic programming
  - records current optimal result for each step through long list or scrolling list
  - initial: size=0 and size=1
  - traverse: update optimal result through the first two results
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        list to store every step of the increment of house results
        """
        size = len(nums)
        if size == 0:
            return 0
        if size == 1:
            return nums[0]
        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, size):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]

    def rob2(self, nums):
        """
        Scrolling list 
        """
        size = len(nums)
        if size == 0:
            return 0
        if size == 1:
            return nums[0]
        dp = [0] * size
        first = nums[0] 
        second = max(nums[0], nums[1])
        for i in range(2, size):
            first, second = second, max(first+nums[i], second)
        return second


if __name__ == '__main__':
    nums = [2, 7, 9, 3, 1]  # output: 12
    S = Solution()
    print(S.rob2(nums))
