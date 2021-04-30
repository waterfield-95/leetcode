"""
2021.4
idea:
1. recursive with cache
    - boundary: res[0]=1, res[x<0]=0
    - recursive: res[x] = sum([res[x-num] for num in nums:])
2. DP (from top to bottom)
    - set dp list
    - dp states equation: dp[x] += dp[x-num] for num in nums
"""

from typing import List
from functools import wraps


class Solution:
    def __init__(self):
        self.cache = {}
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if target < 0:
            return 0
        if target == 0:
            return 1
        res = 0
        for num in nums:
            x = target - num
            if x not in self.cache:
                self.cache[x] = self.combinationSum4(nums, x)
            res += self.cache[x]                
        return res

    def combinnationSum4_dp(self, nums, target):
        dp = [0] * (target+1)
        dp[0] = 1
        res = 0
        for i in range(target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[target]


if __name__ == '__main__':
    nums = [1,2,3]
    target = 4
    S = Solution()
    print(S.combinationSum4_recursive(nums, target))
