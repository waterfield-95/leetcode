from typing import List

class Optimal:
    """
    Time: O(LogN)
    Space: O(1)
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search(left, right, is_first):
            while left <= right:
                mid = left + (right-left) // 2
                
                if nums[mid] == target:
                    if is_first:
                        if mid == left or nums[mid-1] != target:
                            return mid
                        else:
                            right = mid - 1
                    else:
                        if mid == right or nums[mid+1] != target:
                            return mid
                        else:
                            left = mid + 1
                elif nums[mid] > target:
                    # go left
                    right = mid - 1
                else:
                    left = mid + 1
            
            return -1
        
        l = 0
        r = len(nums)-1
        lower = binary_search(l, r, True)
        if lower == -1:
            return [-1, -1]
        upper = binary_search(l, r, False)
        return [lower, upper]
        

class Recursion:
    """
    Time: O(logN)
    Space: O(logN)
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search(left, right, is_first):
            if left > right:
                return -1
            
            mid = left + (right-left) // 2
            if nums[mid] == target:
                if is_first:
                    if mid == left or nums[mid-1] < target:
                        return mid
                    else:
                        return binary_search(left, mid-1, is_first)
                else:
                    if mid == right or nums[mid+1] > target:
                        return mid
                    else:
                        return binary_search(mid+1, right, is_first)
            elif nums[mid] > target:
                # go left to find
                return binary_search(left, mid-1, is_first)
            else:
                return binary_search(mid+1, right, is_first)
        
        lower = binary_search(0, len(nums)-1, True)
        if lower == -1:
            return [-1, -1]
        upper = binary_search(0, len(nums)-1, False)
        
        return [lower, upper]