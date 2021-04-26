"""
2021.4
idea: binary search and greedy algorithm
  - set result boundary of the least weight capacity, binary search to find answer
  - greedy thinking: increment until total_weights is larger than mid of result and then days increment
  - if days is less or equal to D, right bounday is assigned to mid, otherwise left boundary is assigned to mid plus 1
"""


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left)//2  # 向下根除
            total_weights = 0
            days = 1
            for weight in weights:
                total_weights += weight
                if total_weights > mid:
                    total_weights = weight
                    days += 1
            if days <= D:
                right = mid
            else:
                left = mid + 1
        return right
