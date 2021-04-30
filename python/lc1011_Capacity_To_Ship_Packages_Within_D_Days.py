"""
2021.4
idea: binary search and greedy algorithm
  - set result boundary of the least weight capacity, binary search to find answer
  - greedy thinking: increment until total_weights is larger than mid of result and then days increment
  - if days is less or equal to D, right bounday is assigned to mid, otherwise left boundary is assigned to mid plus 1
"""

from typing import List


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

    def official_solution(self, weights, D):
        # set binary search boundary
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            # need is the number of shipping days
            # cur is the total weights during the current day
            need, cur = 1, 0
            for weight in weights:
                if cur + weight > mid:
                    need += 1
                    cur = 0
                cur += weight 
            if need <= D:
                right = mid
            else:
                left = mid + 1
        return left

        
if __name__ == '__main__':
    # weights = [i for i in range(1, 11)] # output: 55
    weights = [i for i in range(1, 11)] # 
    D = 1
    S = Solution()
    print(S.shipWithinDays(weights, D))
