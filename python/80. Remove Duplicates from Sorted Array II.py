"""
2021.4
Similar Problem: 26. Remove Duplicates from Sorted Array

idea:
- two pointer: one of them aims to point to element which will modified, the other is used for traversal of the whole elements
- compare current element whose index is larger than two with the second element before it
  - if they are same, traverse next one
  - if different, modify the first pointer element equal to element pointed by the second pointer
"""

from typing import List

class Solution:
    def removeDuplicates1(self, nums: List[int]) -> int:
      # 26. Remove Duplicates from Sorted Array
        n = len(nums)
        if n < 2:
            return n
        p1 = p2 = 1
        while p2 < n:
            if nums[p1-1] != nums[p2]:
                nums[p1] = nums[p2]
                p1 += 1
            p2 += 1
        return p1

    
    def removeDuplicates(self, nums):
        n = len(nums)
        if n < 3:
            return n
        p1 = p2 = 2
        while p2 < n:
            if nums[p1-2] != nums[p2]:
                nums[p1] = nums[p2]
                p1 += 1
            p2 += 1
        return p1

                

if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    S = Solution()
    print(S.removeDuplicates(nums))
