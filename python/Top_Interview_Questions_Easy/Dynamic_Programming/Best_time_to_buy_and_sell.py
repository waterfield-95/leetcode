"""
2021.10.14
Given a array in which the elements represent the prices in current day. [7,1,5,3,6,4]
- find out the maximum profit between two numbers(days)
"""

from typing import List

class BF:
    """
    TC: O(n^2), TLE
    """
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        for i in range(n):
            for j in range(i+1, n):
                max_profit = max(prices[j] - prices[i], max_profit)

        return max_profit

class OnePass:
    """
    Main two variables: min_price, max_profit which is based on the last min_price we to find the maximim prices
    """
    def maxProfit(self, prices):
        from math import inf
        min_price = float(inf)
        max_profit = 0
        for i, price in enumerate(prices):
            min_price = min(min_price, price)
            max_profit = max(price - min_price, max_profit)
        return max_profit
            



if __name__ == "__main__":
    prices = [7,1,5,3,6,4]  #5
    S = OnePass()
    print(S.maxProfit(prices))
