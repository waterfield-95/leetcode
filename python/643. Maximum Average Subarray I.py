"""
idea: slide window with two pointer, you must figure out the boundary condition
 - boundary: start right pointer with the element of the index of k, and end with k' which is equal to length of nums-list (k < len(nums))
"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k
        total = max_total = sum(nums[:right])
        length = len(nums)
        while right < length:
            total = total - nums[left] + nums[right]
            if total > max_total:
                max_total = total
            left += 1
            right += 1
        return max_total/k
