"""
2021.8
Given an integer array and k, return the kth largest element
idea: 
- quick sort in reverse and return the kth element
"""

from typing import List
import random

class Solution:
    def quicksort(self, nums):
        pivot = random.choice(nums)
        pass
        


    def findKthLargest(self, nums: List[int], k: int) -> int:
        pass
        

if __name__ == '__main__':
    nums = [3,2,3,1,2,4,5,5,6]  # 4
    k = 4
    S = Solution()
    print(S.findKthLargest(nums, k))
    