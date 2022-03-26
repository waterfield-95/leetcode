"""
idea: double pointer, the first one is used for unique element, the second is to traverse all elements in the nums. 
If both value pointed is not equal, swap their value and increment first pointer, and then continue traversal.
"""
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 0
        n = len(nums)
        while right < n:
            if nums[right] == nums[left]:
                right += 1
            else:
                nums[left + 1], nums[right] = nums[right], nums[left + 1]
                right += 1
                left += 1
        return left + 1

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 0
        n = len(nums)
        for right in range(n):
            if nums[right] != nums[left]:
                nums[left + 1] = nums[right]
                left += 1
        
        return left + 1