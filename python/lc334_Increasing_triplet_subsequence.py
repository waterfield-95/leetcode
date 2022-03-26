import math
from typing import List

class Solution:
    """
    TC: O(n)
    Greedy thinking flow to keep track of the first two smallest number and find the third number
    which is bigger than the first two.
    Note: The first two smallest number might not be the triplet subsequence: 1 2 0 4
    """
    def increasingTriplet(self, nums: List[int]) -> bool:
        # greedy to find the first two smallest number, float("inf")
        first_number, second_number = math.inf, math.inf
        for i in range(len(nums)):
            if nums[i] < first_number:
                first_number = nums[i]
            elif nums[i] > first_number and nums[i] < second_number:
                second_number = nums[i]
            elif nums[i] > second_number:
                return True
            
        return False
                
