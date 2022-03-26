# Template for Memorization-DP
"""
func dp(dp_state, memo_dict):
    # check if we have seen this dp_state
    if dp_state in memo_dict:
        return memo_dict[dp_state]
    
    # base case (a case that weknow the answer for already)
    if dp_state is the base case:
        return something like 0 or null
    
    calculate dp(dp_state) from dp(other_state) # sub_state

    save dp_state and result into memo_dict
    return result

func answerToProblem(input):
    return dp(start_state, empty_memo_dict)
"""

from typing import List
from functools import lru_cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def dp(left, right):  # burst all balloons between left and right index inclusive, return the maximum coins obtainable
            # empty -> return 0
            if right - left < 0:
                return 0
            res = 0
            for i in range(left, right+1):
                # mark balloon in i-th index as the last one burst
                gain = nums[left-1] * nums[i] * nums[right+1]
                # burst all the balloon except the i-th one
                remaining = dp(left, i-1) + dp(i+1, right)
                res = max(res, remaining + gain)
            return res
                
                
        nums = [1] + nums + [1]
        return dp(1, len(nums)-2)




