"""
2021.7.2
idea:
1. sort + greedy
"""

from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        sort_cost = sorted(costs)
        sum = 0
        count = 0

        for i in range(len(sort_cost)):
            if sum + sort_cost[i] <= coins:
                sum += sort_cost[i]
                count += 1
            else:
                break
        return count

