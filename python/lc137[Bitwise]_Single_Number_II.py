"""
2021.4
idea: map and bitwise operation
1. hashmap to count occurence times
2. bitwise sum, if the remainder of the bit is equal to 0, this bit is 1
"""

from typing import List

class Solution:
    def numberOf1(self, n):
        if n < 0:
            n = n & 0xffffffff
        temp = 0x00000001
        count = 0
        for i in range(32):
            if n & temp:
                count += 1
            temp = temp << 1
        return count

    def singleNumber_map(self, nums: List[int]) -> int:
        counter = {}
        n = len(nums)
        for num in nums:
            counter[num] = counter.setdefault(num, 0) + 1
        for num, count in counter.items():
            if count == 1:
                return num

    def singleNumber(self, nums):
        res = 0
        for i in range(32):
            total = sum([(num >> i) & 1 for num in nums])
            if total % 3:
                if i == 31:
                    res -= 1 << i
                else:
                    res |= 1 << i 
        return res


if __name__ == '__main__':
    nums = [0, 1, 0, 1, 0, 1, 99]
    S = Solution()
    print(S.singleNumber(nums))
