"""
2021.5
idea:
1. sqrt + power of 2
"""

import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        BIG = 2**31
        return n > 0 and BIG % math.sqrt(n) == 0

    def isPowerOfFour_bitwise(self, n):
        return n>0 and (n&(n-1))==0 and (n & 0xaaaaaaaa)==0


if __name__ == '__main__':
    n = 32
    S = Solution()
    print(S.isPowerOfFour(n))
    print(S.isPowerOfFour_bitwise(n))