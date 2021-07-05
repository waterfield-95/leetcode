"""
2021.7.2
idea:
1. sort + greedy. 
- Given cost list and total coins, in each step we need to get the local maximum cost, 
and then it‘s substracted by the total coins. Iteration for the rest of coins larger than current bar cost

2. count-array + greedy
- count-array: index -> cost and element -> frequency, time complexity is O(n) instead of O(nlog) 
"""

from typing import List
import random

# sort + greedy
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

    def quick_sort(self, l):
        if len(l) < 2:
            return l
        pivot = random.choice(l)
        less = []
        more = []
        equal = []
        for x in l:
            if x > pivot:
                more.append(x)
            elif x < pivot:
                less.append(x)
            else:
                equal.append(x)
        return self.quick_sort(less) + equal + self.quick_sort(more)

# Count array + greedy
class Solution2:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        frequency = [0 for _ in range(int(1e5+1))]
        for cost in costs:
            frequency[cost] += 1
        
        count = 0
        for i in range(1, len(frequency)):
            if coins >= i:
                i_count = min(frequency[i], coins/i)
                count += i_count
                coins  -= i * i_count
            else:
                break
        return count


if __name__ == '__main__':
    # costs = [10, 6, 8, 7, 7, 8]
    costs = [1,3,2,4,1]
    coins = 7
    S = Solution()
    print(S.maxIceCream(costs, coins))
    print(S.quick_sort(costs))

    S2 = Solution2()
    print(S2.maxIceCream(costs, coins))