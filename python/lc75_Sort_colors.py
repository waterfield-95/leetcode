from typing import List
import random

class Solution:
    """
    Time: O(N)
    Space: O(1)
    """
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p0, p2 = 0, n-1
        i = 0
        while i <= p2:
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            else:
                i += 1
            
                

class QuickSort:
    """
    Time: O(NlogN)
    Space: O(1)
    """
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quick_sort(nums, 0, len(nums)-1)
    
    def quick_sort(self, nums, start, end):
        if start < end:
            leftend = self.partition(nums, start, end)
            self.quick_sort(nums, start, leftend)
            self.quick_sort(nums, leftend+1, end)
    
    def partition(self, nums, start, end):
        left, right = start, end
        pivot = random.choice(nums[start:end+1])
        while True:
            while nums[left] < pivot:
                left += 1
            while nums[right] > pivot:
                right -= 1
            
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            else:
                return right
        
        