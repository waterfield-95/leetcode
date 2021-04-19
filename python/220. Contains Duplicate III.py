"""
2021.4
idea:
1. bisection
  - traverse element, judge whether or not there are elements in the range of [num-t, num+t] in the list of [max(0, i-k), i]
  - find idx which is larger than num-t in the sorted window.
  - and then 
"""

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        from bisect import bisect_left, insort_left
        window = []
        for i, num in enumerate(nums):
            idx = bisect_left(window, num-t)
            if idx < len(window) and window[idx] <= num+t:
                return True

            insort_left(window, num)
            if i >= k:
                window.remove(nums[i-k])
        return False
