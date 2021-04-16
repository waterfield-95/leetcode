"""
2021.4
idea: DP, recursive
1. DP
  - state transition equation: dp[n] = dp[n-1] + dp[n-2]
  - boundary: dp[1]=1, dp[2]=2
  - validation: dp[3], d[4], dp[5] satisfied above condition
2. recursive
  - similar with DP (Essentially the same)
  - same with Fibonacci sequence
"""

from functools import wraps
import time


def func_timer(func):
    @wraps(func)
    def wrapper(*args):
        t1 = time.time()
        res = func(*args)
        interval = time.time() - t1
        print(interval)
        return res
    return wrapper


def cache(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            pass
        else:
            cache[args] = func(*args)
        return cache[args]
    return wrapper


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            first = 1
            second = 2
            for i in range(3, n + 1):
                first, second = second, first + second
            return second

    def climbStairs2(self, n, cache=None):
        if cache is None:
            cache = {}
        if n in cache:
            return cache[n]
        if n == 1:
            return 1
        if n == 2:
            return 2
        cache[n] = self.climbStairs2(n - 1, cache) + self.climbStairs2(
            n - 2, cache)
        return cache[n]

    @cache
    def climbStairs3(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs3(n - 1) + self.climbStairs3(n - 2)


if __name__ == '__main__':
    n = 5
    S = Solution()
    t1 = time.time()
    print(S.climbStairs3(n), time.time() - t1)

