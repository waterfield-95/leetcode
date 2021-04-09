"""
2021.4
idea: binary search
1. the minimum of sorted array divide the whole array to two monotonic interval
  - in the monotonic interval, we could use binary search to find target
  - if nums[mid] >= nums[0], now the mid is in the first interval; otherwiese, in the second interval
  - When mid in the monotonic interval, we need to consider target position, which means if the target is located before or after mid, and then change left and right pointer
"""

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            # 当mid在前半段单调增区间
            if nums[mid] >= nums[0]:
                # target 在left和mid之间
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
