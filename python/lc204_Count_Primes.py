"""
2021.4
idea: 埃塞法，将质数平方之后的倍数都设为合数
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        # O(nloglogn) Eratosthenes
        prime_list = [i for i in range(n)]
        count = 0
        for i in range(2, n):
            if prime_list[i] != 0:
                count += 1
                if i*i < n:
                    for j in range(i*i, n, i):
                        prime_list[j] = 0
        return count
      
    
