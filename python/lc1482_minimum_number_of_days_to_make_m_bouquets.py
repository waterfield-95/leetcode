"""
2021.5
idea: binary search + 1-time traverse with 2 counter
    - checkDay function to judge if the given day is satisfied
    - based on binary search, we could find the minimum day between the minimum and maximum of the bloomDay 
"""

from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
    
        def checkDay(day):
            bouquests = flowers = 0
            for bloom_day in bloomDay:
                if bloom_day <= day:
                    flowers += 1
                    if flowers == k:
                        bouquests += 1
                        flowers = 0
                        if bouquests == m:
                            return True
                else:
                    flowers = 0
            return False

        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = left + (right - left)//2
            if checkDay(mid):
                right = mid
            else:
                left = mid + 1
        return right
        

if __name__ == '__main__':
    bloomDay = [12,83,63,97,20,1,70,95,22,48,47,60,63,64,79,43,95,14,11,71,83,10,71,47,95,23,23,79,24,46,94,37]
    m = 4
    k = 7
    S = Solution()
    print(S.minDays(bloomDay, m, k))
    