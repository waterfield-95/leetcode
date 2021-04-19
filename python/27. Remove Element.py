"""
2021.4
idea: double pointer
1. respectively represent output and input pointer
  - left points the next satisfied number
  - right points the traverse number
2. traverse from the beginning and ending: more efficient
  - keep the correct ouput after left pointer assignment, notice "while left <= right"
  - we don't care about the val data if it is coverd
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        return left
      

class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return left
