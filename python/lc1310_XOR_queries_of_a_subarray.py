"""
2021.5
idea: 
    - XOR mathematical properties:
        - commutativity: a^b=b^a
        - associativity: a^b^c = a^(b^c)
"""

from typing import List

class Solution:
    def xorQueries(self, arr, queries):
        prefix_sum = [arr[0]]
        for i in range(1, len(arr)):
            prefix_sum.append(prefix_sum[i-1]^arr[i])
        n = len(queries)
        res = [0] * n
        for j, (left, right) in enumerate(queries):
            if left == 0:
                res[j] = prefix_sum[right]
            else:
                res[j] = prefix_sum[right] ^ prefix_sum[left-1]
        return res 

    def xorQueries_bf(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n_queries = len(queries)
        res = [0] * n_queries
        for i, (l, r) in enumerate(queries):
            res[i] = 0
            for j in range(l, r+1):
                res[i] ^= arr[j]
        return res
        

if __name__ == '__main__':
    arr = [1,3,4,8]
    queries = [[0,1], [1,2], [0,3], [3,3]]
    S = Solution()
    print(S.xorQueries(arr, queries))
