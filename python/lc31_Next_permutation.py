from typing import List

class Solution:
    """
    Time: O(N)
    Space: O(1)
    """
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse_ls(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            return nums
            
        # iterate over nums starting from the end
        # find the first one i less than the next value
        n = len(nums)
        replaced = n - 2
        while replaced >= 0 and nums[replaced] >= nums[replaced + 1]:
            replaced -= 1
        
        if replaced >= 0:
            # find the first value greater than replaced behind it started from the end
            replace = n - 1
            while nums[replace] <= nums[replaced]:
                replace -= 1
            nums[replace], nums[replaced] = nums[replaced], nums[replace]
        
        # reverse for converting the largest string to smallest string
        return reverse_ls(nums, replaced + 1, n - 1)
            
            