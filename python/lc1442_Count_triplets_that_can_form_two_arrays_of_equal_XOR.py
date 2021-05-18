"""
2021.5
idea: Prefix XOR, S[i] = arr[0]^...^arr[i-1]
1. traverse k for 1 loop
    - calculate prefix XOR sum
    - maintenance two variable: 
        - cnt, count of prefix XOR sum 
        - total, total of index i where prefix XOR sum is the same
"""

from typing import List
from collections import Counter

class Solution:
    def countTriplets_loop3(self, arr: List[int]) -> int:
        n = len(arr)
        # 前n相的异或和，初始化前0相异或和为0
        pre = [0]
        for num in arr:
            pre.append(pre[-1] ^ num)
        
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j, n):
                    if pre[i] == pre[k+1]:
                        ans += 1
        return ans
    
    def countTriplets_loop2(self, arr):
        n = len(arr)
        pre = [0]
        for num in arr:
            pre.append(pre[-1] ^ num)
        
        ans = 0
        for i in range(n):
            for k in range(i+1, n):
                if pre[i] == pre[k+1]:
                    ans += k - i
        return ans

    def countTriplets_loop1(self, arr):
        n = len(arr)
        s = [0]
        for val in arr:
            s.append(s[-1] ^ val)
        
        cnt, total = Counter(), Counter()
        ans = 0
        for k in range(n):
            if s[k + 1] in cnt:
                ans += cnt[s[k + 1]] * k - total[s[k + 1]]
            cnt[s[k]] += 1
            total[s[k]] += k
        return ans

    def countTriplets(self, arr: List[int]) -> int:
        cnt, total = Counter(), Counter()
        s = ans = 0
        for k, val in enumerate(arr):
            next_sum = s ^ val
            if next_sum in cnt:
                ans += cnt[next_sum] * k - total[next_sum]
            cnt[s] += 1
            total[s] += k
            s = next_sum
        return ans


if __name__ == '__main__':
    arr = [2,3,1,6,7]   # 4
    S = Solution()
    print(S.countTriplets(arr))
    