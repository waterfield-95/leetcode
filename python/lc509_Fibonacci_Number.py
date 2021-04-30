'''
date: 201011
idea: recur+hashmap (memerization to reduce repeated calculation)
'''

class Solution:
    def fib(self, N: int) -> int:
        if N==0: return 0
        if N==1: return 1
        return self.fib(N-2) + self.fib(N-1)
    

class Solution2:
    def fib(self, N: int) -> int:
        cache = {}
        def mem_fib(N): 
            if N in cache:
                return cache[N]

            if N < 2:
                return N
            else:
                res = mem_fib(N-1) + mem_fib(N-2)
                cache[N] = res
                return res

        return mem_fib(N)
