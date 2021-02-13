"""
2021.2
idea: 
1. set subtraction due to the deduplication of a set
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res_set = set(i for i in range(1, n+1))
        nums_set = set(nums)
        return res_set - nums_set
