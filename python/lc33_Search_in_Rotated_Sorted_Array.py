from typing import List

"""
2021.4
idea: binary search
1. the minimum of sorted array divide the whole array to two monotonic interval
  - in the monotonic interval, we could use binary search to find target
  - if nums[mid] >= nums[0], now the mid is in the first interval; otherwiese, in the second interval
  - When mid in the monotonic interval, we need to consider target position, 
  which means if the target is located before or after mid, and then change left and right pointer
"""

class Optimal:
    """
    Time: O(LogN)
    Space: O(1)
    """
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1
        while left <= right:
            mid = left + (right-left)//2
            print(mid)
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] >= nums[left]:
                    if nums[left] <= target < nums[mid]:  # monotonous
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    if nums[right] >= target > nums[mid]:  # monotonous subarray
                        left = mid + 1
                    else:
                        right = mid - 1
        return -1
    
# [4,5,6,7,0,1,2], target=0 -> 7,i=4 7>4 and 0<7 go right -> [...0,1,2],1>0 and 0<1 go left, [0] we got it

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        
        def find_rotate_index(left, right):
            if nums[left] <= nums[right]:
                return 0
            
            while left <= right:
                pivot = left + (right - left) // 2
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot - 1
                    else:
                        left = pivot + 1

        r_pos = find_rotate_index(left, right)
        if r_pos != 0:
            if target == nums[0]:
                return 0
            elif target > nums[0]:
                right = r_pos - 1
            else:
                left = r_pos
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            else:
                if target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
            
    
# nums = [4,5,6,7,0,1,2], target = 0
                
        

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            # 当mid在前半段单调增区间
            if nums[mid] >= nums[0]:
                # target 在left和mid之间
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        def find_minimum_index(left, right):
            if nums[left] <= nums[right]:
                return left
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > nums[mid + 1]:
                    return mid + 1
                else:
                    if nums[mid] >= nums[left]:
                        left = mid + 1
                    else:
                        right = mid - 1
        
        return find_minimum_index(0, len(nums) - 1)

if __name__ == "__main__":
    S = Solution1()
    nums = [4,5,1,2,3]
    print(S.search(nums, 1))