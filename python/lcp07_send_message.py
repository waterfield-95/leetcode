from typing import List
from collections import defaultdict


# DFS in graph: boundary condition to modify recursion sum variable
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        map = defaultdict(list)
        for a,b in relation:
            map[a].append(b)

        count = 0

        def dfs(idx, k):
            nonlocal count
            if k == 0:
                if idx==n-1: count+= 1
                return 

            for next in map[idx]:
                dfs(next, k-1)

        dfs(0, k)
        return count
            

if __name__ == '__main__':
    n = 5
    relation = [[0,2], [2,1], [3,4], [2,3], [1,4], [2,0], [0,4]]
    k = 3
    S = Solution()
    print(S.numWays(n, relation, k))
