"""
2021.7.4
idea: count array
"""

from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count_array = [-1] + [0 for _ in range(len(nums))]
        for i, num in enumerate(nums):
            count_array[num] += 1

        res = [0, 0]
        for i, count in enumerate(count_array):
            if count == 2:
                res[0] = i
            if count == 0:
                res[1] = i
        return res
        