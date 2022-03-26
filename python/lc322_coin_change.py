from typing import List
import collections
import math
from functools import lru_cache
# lru_cache(None)

class DP_TopDown:
    """
    Time: O(S*N), S -> worst case, use 1 coin, tree depth is S
    So you would solve S sub-problems which is computed with n iterations
    Space: O(S), height of tree is S in the worst case only using 1-denomination coin
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = collections.defaultdict(int)
        
        def dp(amount):
            if amount in mem:
                return mem[amount]
            
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            
            min_cnt = math.inf 
            for coin in coins:
                cnt = dp(amount - coin)
                if cnt == -1:
                    continue
                min_cnt = min(min_cnt, cnt + 1)
            
            mem[amount] = min_cnt if min_cnt != math.inf else -1
            return mem[amount]
                
        dp(amount)
        
        return mem[amount]

class BottomUp:
    """
    Time: O(S*N)
    Space: O(S)
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        
        # base case
        dp[0] = 0
        
        for i in range(1, len(dp)):
            for coin in coins: 
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        print(dp)        
        return dp[amount] if dp[amount] != amount+1 else -1

# coins = [1,2,5], amount = 11
# [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]