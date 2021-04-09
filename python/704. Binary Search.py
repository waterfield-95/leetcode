"""
2021.4 classic topic
idea:
1. two pointer with left and right, while left is less and equal to right, calculate mid of them and judge whether or not it is target number
2. recursive, binary_search, remember to update left and right pointer with increment or decrement
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
      low, high = 0, len(nums)-1
      while low <= high:
          # high - low 不用加法防止溢出
          mid = low + (high - low) // 2
          if nums[mid] == target:
              return mid
          elif nums[mid] > target:
              high = mid-1
          else:
              low = mid+1
      return -1
    
    def search2(self, nums: List[int], target: int) -> int:
        def binary_search(nums, target, left, right):
            if left <= right:
                # 加减优先级高于移位运算，所以加括号
                mid = left + ((right - left) >> 1)
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    return binary_search(nums, target, left, mid-1)
                else:
                    return binary_search(nums, target, mid+1, right)
            else:
                return -1
        return binary_search(nums, target, 0, len(nums)-1)
