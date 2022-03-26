from typing import List

"""
Notice: nums[i] != nums[i + 1] for all valid i.
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
                
        return left

class Recursion:
    """
    Time: O(logN)
    Space: O(logN) -> recursion tree depth
    """
    def findPeakElement(self, nums: List[int]) -> int:
        
        def binary_search(left, right):
            if right == left:
                return left
            
            mid = left + (right-left) // 2
            
            # if mid point lies on a rising slope, go right side to find out peak point, 
            # otherwise throw out current point and go left side
            if nums[mid] < nums[mid+1]:
                return binary_search(mid+1, right)
            else:
                return binary_search(left, mid)
                
        ret =  binary_search(0, len(nums)-1)
        return ret

if __name__ == "__main__":
    nums = [1,1,1,2]
    S = Recursion()
    print(S.findPeakElement(nums))
