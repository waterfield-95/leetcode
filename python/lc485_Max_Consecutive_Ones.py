"""
2021.2
idea:
1. traverse one time, set two variables which respectively are count and max_count
 - when we meet 1, we need to accumulate.Otherwise, we need to calculate the maximum of max_count and count
 - Don't forget the special situation, for instance, [1] or [0, 1, 0, 1, 1], at this time, we need to consider the count variable after the whole traverse. 
 - So, we need to refresh the max_count when we return the result
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        return max(max_count, count)
