"""
2021.4
idea: 
1. minimum heap through python heapq model
  - build heap list and seen list which records visited ugly number
  - traverse n, each time get current minimum value, and finally get destination cur and return it.
  - multiply cur with 2,3,5 factor and then add to seen list if they are not in it.
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        import heapq
        heap = [1]
        seen = {1}
        for num in range(n):
            cur = heapq.heappop(heap)
            for factor in [2,3,5]:
                new = cur * factor
                if new not in seen:
                    heapq.heappush(heap, new)
                    seen.add(new)
        return cur
      
