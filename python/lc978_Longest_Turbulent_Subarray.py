"""
idea: slide window with 2 pointer
- set last_state and current_state and consider the initial state
- consider state of pair elements which are equal
"""

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, 1
        last_flag = 'init'
        res = 1
        if n < 2:
            return res
        while right < n:
            # cf = True if increasing state
            if arr[right-1] < arr[right]:
                current_flag = 'up'
            elif arr[right - 1] > arr[right]:
                current_flag = 'down'
            else:
                last_flag = 'init'
                right += 1
                left = right - 1
                continue
            
            if current_flag == last_flag:
                left = right - 1
            last_flag = current_flag
            right += 1
            res = max(res, right-left)
        return res
