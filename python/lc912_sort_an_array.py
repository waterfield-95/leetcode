from typing import List
import random

"""
2021.5
idea:
1. quick sort
"""

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        pivot = random.choice(nums)
        equal = [num for num in nums if num == pivot]
        less = [num for num in nums if num < pivot]
        more = [num for num in nums if num > pivot]
        return self.sortArray(less) + equal + self.sortArray(more)