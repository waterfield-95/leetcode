"""
2021.4
idea: DP
  - considering last one and the first one
  - divide to two part, respectively get the optimal result and get the better one from both
  - through scrolling method to get optimal solution, first and second pointer, the third solution is get the maximum between the first plus current number and the second one
"""


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
