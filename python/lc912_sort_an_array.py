from typing import List, SupportsAbs
import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums)-1)
        return nums
    
    def quick_sort(self, A, start, end):
        if start < end:
            leftend = self.Hoare_partition(A, start, end)
            self.quick_sort(A, start, leftend)
            self.quick_sort(A, leftend+1, end)
            
    def Hoare_partition(self, A, start, end):
        """
        inclusive of start and end
        Return pivot and ensure that 
        - the elements in left part of pivot are less than or equal to pivot; 
        - those in right region are greater than or equal to pivot
        - Finally, return the idx of 
        """
        import random
        pivot = random.choice(A[start:end+1])
        left, right = start, end
        while True:
            while A[left] < pivot:
                left += 1
            while A[right] > pivot:
                right -= 1
            
            if left < right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
            else:
                return right
    
    

class QuickSort:
    """
    In place
    By using Hoare partition, inclusive start and end element
    """
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums)-1)
        return nums
    
    def quick_sort(self, A, start, end):
        """
        Sort in place
        """
        if start >= end:
            return
        
        left, right = start, end
        pivot = A[start+ (end - start)//2]  # set the mid-index element as pivot
        
        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1
            
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
            
        self.quick_sort(A, start, right)
        self.quick_sort(A, left, end)

class QuickSort1:
    """
    Not in place, just for easy understanding
    """
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        pivot = random.choice(nums)
        equal = [num for num in nums if num == pivot]
        less = [num for num in nums if num < pivot]
        more = [num for num in nums if num > pivot]
        return self.sortArray(less) + equal + self.sortArray(more)


if __name__ == "__main__":
    nums = [5,2,3,1]
    S = Solution()
    print(S.sortArray(nums))