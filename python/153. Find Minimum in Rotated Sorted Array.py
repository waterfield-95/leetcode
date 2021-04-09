"""
2021.4
idea: binary search (sorted nums)
1. find pivot which is middle of left and right, compare value of pivot with the right value
  - if n[pivot] > n[right], the minimum is in the right of left pointer, so let left = pivot + 1
  - if n[pivot] <= n[right], let right = pivot
  - when it comes to condition that n[pivot] = n[right], which means left = right, so there is no necessary to judge this condition
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = (high + low) // 2
            if nums[pivot] < nums[high]:
                high = pivot 
            else:
                low = pivot + 1
        return nums[low]
