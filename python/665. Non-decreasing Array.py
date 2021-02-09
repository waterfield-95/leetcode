"""
idea: 
1. Keep the nums list non-decreasing list, set a counter to accumulate when nums[i] larger than nums[i+1]
- And then in order to keep non-decreasing, we need to modify the value of i+1 as the value of i if i > 0 and nums[i-1] > nums[i+1],
otherwise, we'll do  nothing because next time counter accumulate and larger than 1, so return False
"""

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        cnt = 0
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                cnt += 1
                if cnt > 1:
                    return False
                if i > 0 and nums[i-1] > nums[i+1]:
                    nums[i+1] = nums[i]
        return True
