"""
2021.10.12
Each time you can either climb 1 or 2 steps, how many distinct ways can you climb to the top
"""

class BF:
    """
    O(2^n), many duplicate calculation
    """
    def climbStairs_bottom(self, n):
        """
        brute force, time limited error
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n-2)
    
    def climbStairs_up(self, n):
        """
        in order, go up the stairs, TLE
        """
        
        def upstair(i, n):
            if i > n:
                return 0
            if i == n:
                return 1
            
            return upstair(i+1, n) + upstair(i+2, n)
        
        return upstair(0, n)

class Memo:
    """
    O(n)
    """
    def climbStairs_dict(self, n):
        """
        Dict as memo,TLE
        """
        from collections import defaultdict
        counter = defaultdict(int)
        
        def upstair(i, n):
            nonlocal counter
            if i > n:
                return 0
            if i == n:
                return 1
            
            if i not in counter.items():
                counter[i] = upstair(i+1, n) + upstair(i+2, n)
            return counter[i]

        return upstair(0, n)

    def climbStairs_array(self, n):
        """
        memo array faster than counter;
        we could use either nonlocal or recurrence with memo parameter
        """
        memo = [0] * (n+1)
    
        def upstair(i, n):  # def upstair(i, n, memo)
            nonlocal memo
            if i > n:
                return 0
            if i == n:
                return 1
            
            if memo[i] == 0:
                memo[i] = upstair(i+1, n) + upstair(i+2, n)
            return memo[i]

        return upstair(0, n)


class DP:
    """
    O(n)
    - the total number of ways to get on the ith step is equal to sum of (i-1)th step and (i-2)th step
    - dp array would use extra space, while two variable would be more efficient
    """
    def climbStairs_array(self, n):
        if n == 1:
            return 1
        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 2
        for i in range(3, len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    def climbStairs(self, n):
        if n == 1:
            return 1
        first, second = 1, 2
        for i in range(3, n+1):
            first, second = second, first+second
        return second
            
        

if __name__ == '__main__':
    n = 5   #8
    S = DP()
    print(S.climbStairs(n))