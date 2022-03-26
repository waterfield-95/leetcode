from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        combination = []
        
        def backtrack(first=0):
            if first == len(nums):
                # nums[:] foo invokes slice assignment on the object that nums refer to
                # thus making the contents of the original object a copy of the contents of foo
                combination.append(nums[:])
                return
            
            for i in range(first,len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1)
                nums[first], nums[i] = nums[i], nums[first]
        
        backtrack()
        return combination
        