'''
date: 201011
idea: recur
'''

class Solution:
    def fib(self, N: int) -> int:
        if N==0: return 0
        if N==1: return 1
        return self.fib(N-2) + self.fib(N-1)
