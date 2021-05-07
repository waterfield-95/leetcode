from typing import List
from collections import Counter
import random

"""
2021.5
idea: DP
"""

class Solution:
    def deleteAndEarn_official1(self, nums):
        """
        set total array, enumerate continues number with an interval of 1.
            - index: number in nums
            - value: sum of same number in nums
        And use rob house solution to solve it.
        """
        max_val = max(nums)
        total = [0] * (max_val + 1)
        for val in nums:
            total[val] += val

        def rob(nums):
            size = len(nums)
            first, second = nums[0], max(nums[0], nums[1])
            for i in range(2, size):
                first, second = second, max(first+nums[i], second)
            return second
        return rob(total)

    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        sorted_nums = self.quickSort(nums)
        counter = Counter(sorted_nums)
        sums = [(num, num*count) for num, count in counter.items()]

        m = len(sums)
        first = sums[0][1]
        if sums[1][0] == sums[0][0] + 1:
            second = max(first, sums[1][1])
        else:
            second = first+sums[1][1]

        for i in range(2, m):
            if sums[i][0] == sums[i-1][0] + 1:
                first, second = second, max(second, first + sums[i][1])
            else:
                first, second = second, second + sums[i][1]
        return second

    def quickSort(self, nums):
        if len(nums) == 0:
            return []
        pivot = random.choice(nums)
        equal = [num for num in nums if num == pivot]
        less = [num for num in nums if num < pivot]
        more = [num for num in nums if num > pivot]
        return self.quickSort(less) + equal + self.quickSort(more)
        


if __name__ == '__main__':
    # nums = [3, 4, 2]    # 6
    # nums = [3, 1]   # 4
    nums = [2,2,3,3,3,4]    # 9
    S = Solution()
    print(S.deleteAndEarn(nums))
    # print(S.quickSort(nums))