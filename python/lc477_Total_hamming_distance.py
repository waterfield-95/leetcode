"""
2021.5
idea:
    - Binary bit to get i bit
        - (val >> i) & 1
        - tmp = 0x00000001, x & tmp, tmp <<= 1
"""

from typing import List

class Solution:
    def number_of_1(self, x):
        x = x & 0xffffffff
        tmp = 0x00000001
        c = 0
        for i in range(32):
            if x & tmp != 0:
                c += 1
            tmp <<= 1   
        return c

    def hammingDistance(self, x, y):
        xor_ = x ^ y
        return self.number_of_1(xor_)
        
    def totalHammingDistance_BF(self, nums: List[int]) -> int:
        n = len(nums)
        sum_ = 0
        for i in range(n):
            for j in range(i, n):
                sum_ += self.hammingDistance(nums[i], nums[j])
        return sum_

    def totalHammingDistance(self, nums):
        tmp = 0x00000001
        total = 0
        n = len(nums)
        for i in range(32):
            c1 = 0
            for num in nums:
                if num & tmp:
                    c1 += 1
            total += c1 * (n - c1)
            tmp <<= 1
        return total

    def totalHammingDistance_official(self, nums):
        n = len(nums)
        ans = 0
        for i in range(30):
            c = sum((val >> i) & 1 for val in nums)
            ans += c * (n-c)
        return ans
                

    
if __name__ == '__main__':
    nums = [4, 14, 4, 14]   # 8
    S = Solution()
    print(S.totalHammingDistance_BF(nums))
    print(S.totalHammingDistance(nums))
    print(S.totalHammingDistance_official(nums))
