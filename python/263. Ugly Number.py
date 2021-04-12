"""
2021.4
idea: factorization until prime number
  - if final number is equal to 1, return True, which means n is ugly number
"""

class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        for factor in [2,3,5]:
            while n % factor == 0:
                n /= factor
        return n == 1
