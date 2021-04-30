"""
2021.4
idea: binary search (sorted nums)
1. find pivot which is middle of left and right, compare value of pivot with the right value
  - if n[pivot] > n[right], the minimum is in the right of left pointer, so let left = pivot + 1
  - if n[pivot] <= n[right], let right = pivot
  - when it comes to condition that n[pivot] = n[right], which means left = right, so there is no necessary to judge this condition
"""


from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        while low < high:
            pivot = (low + high) // 2
            if nums[pivot] < nums[high]:
                high = pivot
            else:
                low = pivot + 1
        return nums[low]
    
    def findMin_lt(self, nums: List[int]) -> int:    
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = (high + low) // 2
            if nums[pivot] < nums[high]:
                high = pivot 
            else:
                low = pivot + 1
        return nums[low]

    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            # high - low 不用加法防止溢出
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
        return -1

    def search2(self, nums: List[int], target: int) -> int:
        def binary_search(nums, target, left, right):
            if left <= right:
                mid = left + ((right - left) >> 1)
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    return binary_search(nums, target, left, mid-1)
                else:
                    return binary_search(nums, target, mid+1, right)
            else:
                return -1
        return binary_search(nums, target, 0, len(nums)-1)

        

if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 9
    S = Solution()
    # print(S.findMin(nums))
    print(S.search2(nums, target))