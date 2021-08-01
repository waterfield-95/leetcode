"""
2021.8
idea: Given binary matrix, return the indices of the k weakest rows
"""

from typing import List
from collections import defaultdict
import heapq

class Solution:
    """
    counter + sort
    O(n^2 + nlogn)
    """
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        counter = defaultdict(int)
        for i in range(len(mat)):
            counter[i] = 0
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    counter[i] += 1
                else:
                    continue

        sl = sorted(counter.items(), key=lambda x: (x[1], x[0]))
        ans = [sl[i][0] for i in range(k)]
        return ans

class DichotomyHeap:
    """
    Binary search to record number of 1
    Heap to sort, by multi-index sort [(1,2), (2,3), (2,1)]
    Complexity: O(nlogn + klogn)
    """
    def kWeakestRows(self, mat, k):
        m, n = len(mat), len(mat[0])
        power = []
        for i in range(m):
            l, r = 0, n-1
            pos = -1
            while l <= r:
                mid = l + (r-l) // 2
                if mat[i][mid] == 1:
                    l = mid + 1
                    pos = mid
                else:
                    r = mid - 1
            power.append((pos+1, i))
        
        heapq.heapify(power)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(power)[1])
        return ans
        

if __name__ == '__main__':
    mat = [[1,0],[0,0],[1,0]]
    k = 2
    S = Solution()
    S1 = DichotomyHeap()
    print(S.kWeakestRows(mat, k))
    print(S1.kWeakestRows(mat, k))
    