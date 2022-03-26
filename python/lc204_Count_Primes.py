from math import sqrt

"""
2021.4
idea: 埃塞法，将质数平方之后的倍数都一定是non-prime
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        primes = [1] * n
        primes[0] = primes[1] = 0
        for i in range(2, int(sqrt(n)) + 1):
            if primes[i] != 0:
                for j in range(i**2, n, i):
                    primes[j] = 0
        
        return sum(primes)
        
      
    
