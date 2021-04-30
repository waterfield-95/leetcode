"""
idea: double pointer, the first one is used for unique element, the second is to traverse all elements in the nums. 
If both value pointed is not equal, swap their value and increment first pointer, and then continue traversal.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        pointer = 0
        for i in range(length):
            if nums[i] == nums[pointer]:
                continue
            else:
                pointer += 1
                temp = nums[pointer]
                nums[pointer] = nums[i]
                nums[i] = temp
        return pointer + 1
