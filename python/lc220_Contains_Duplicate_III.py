"""
2021.4
idea:
1. bisection
  - traverse element, judge whether or not there are elements in the range of [num-t, num+t] in the list of [max(0, i-k), i]
  - find idx which is larger than num-t in the sorted window.
  - and then 
"""

from typing import List
import bisect
from sortedcontainers import SortedList


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

    def containsNearbyAlmostDuplicate2(self, nums: List[int], k: int, t: int) -> bool:
        # O(N logk)
        window = SortedList()
        for i in range(len(nums)):
            # len(window) == k
            if i > k:
                window.remove(nums[i - 1 - k])
            window.add(nums[i])
            idx = bisect.bisect_left(window, nums[i])
            if idx > 0 and abs(window[idx] - window[idx-1]) <= t:
                return True
            if idx < len(window) - 1 and abs(window[idx+1] - window[idx]) <= t:
                return True
        return False


if __name__ == '__main__':
    S = Solution()
    nums = [1, 5, 9, 1, 5 ,9]
    k = 2   # window width
    t = 3   # diff
    print(S.containsNearbyAlmostDuplicate2(nums, k, t))

