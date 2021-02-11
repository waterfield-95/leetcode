"""
idea: heapq to get Kth element without the help of sorted operation(O(NlogN))
- python: heapq function, heapify a list to heap inplace without return
- stream means that we need a function of add to operate an array due to the dynamic change
- we need to maintain a heap with k elements
"""

import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.que = nums
        heapq.heapify(self.que)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.que, val)
        while len(self.que) > self.k:
            heapq.heappop(self.que)
        return self.que[0]
