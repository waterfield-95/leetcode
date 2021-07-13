"""
2021.7
idea: Given an integer array and target, by adding one of symbols +/- before number
to get target, return the total of possibility
"""

from memoization import cached
from typing import List


# Limited Time Exceeded
class Solution:
    @cached
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            if target == 0:
                return 1
            else:
                return 0
        count = self.findTargetSumWays(nums[1:], target-nums[0]) + self.findTargetSumWays(nums[1:], target+nums[0])
        return count

# Limited Time Exceeded
class backtrace:
    def __init__(self) -> None:
        self.cnt = 0

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.backtracking(nums, target, 0, 0)
        return self.cnt

    def backtracking(self, nums, target, idx, sum):
        if idx == len(nums):
            if sum == target:
                self.cnt += 1
        else:
            self.backtracking(nums, target, idx+1, sum + nums[idx])
            self.backtracking(nums, target, idx+1, sum - nums[idx])


class DP:
    def findTargetSumWays(nums, target):
        pass


if __name__ == '__main__':
    nums = [5,2,2,7,3,7,9,0,2,3]
    target = 9
    S = Solution()
    print(S.findTargetSumWays(nums, target))