"""
2021.4
idea: DP
  - considering last one and the first one
  - divide to two part, respectively get the optimal result and get the better one from both
  - through scrolling method to get optimal solution, first and second pointer, the third solution is get the maximum between the first plus current number and the second one
"""
from typing import List

class Solution:
    """
    Circle degrades to two sequence sub-problems which are num[0:n-2] and num[1:n]
    """
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        res = max(self.helper(nums[:n-1]), self.helper(nums[1:]))
        return res
    
    def helper(self, nums: List[int]) -> int:
        cur = 0
        prev = 0
        for num in nums:
            tmp = cur
            cur = max(cur, prev + num)
            prev = tmp 
        return cur


class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_range(nums, start, end):
            first = nums[start]
            second = max(nums[start], nums[start+1])
            for i in range(start+2, end+1):
                first, second = second, max(first+nums[i], second)
            return second

        size = len(nums)
        if size == 1:
            return nums[0]
        elif size == 2:
            return max(nums[0], nums[1])
        else:
            return max(rob_range(nums, 0, size-2), rob_range(nums, 1, size-1))
