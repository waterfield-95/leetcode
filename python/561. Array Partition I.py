"""
2021.2
idea: sort list and combine the smaller number into a pair due to maximum of min(pair)
"""

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 原地排序
        nums.sort()
        return sum(nums[::2])
        
