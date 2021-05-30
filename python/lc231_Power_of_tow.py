"""
2021.5
idea: 
1. bitwise, number of 1, n&(n-1) == 0
2. divisor, 2**31 % n == 0
"""


class Solution:
    def number_of_1(self, n):
        c = 0
        n = n & 0xffffffff
        tmp = 0x00000001
        for i in range(32):
            if n & tmp != 0:
                c += 1
            tmp <<= 1
        return c
            
    def isPowerOfTwo_1(self, n: int) -> bool:
        if n <= 0:
            return False
        if self.number_of_1(n) > 1:
            return False
        else:
            return True

    def isPowerOfTwo(self, n):
        BIG = 2**31
        return n > 0 and BIG % n == 0

    def isPowerOfTwo_bitwise(self, n):
        return n > 0 and n&(n-1) == 0


if __name__ == '__main__':
    n = 16
    S = Solution()
    print(S.isPowerOfTwo(n))
        
        