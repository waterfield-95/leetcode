"""
2021.5
idea: Prefix sum
1. sort
    - prefix sum notices pre sum does not include current element, and we need to add 0 to the begin.
2. quick select
"""

from typing import List

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        pre = [[0] * (n+1) for _ in range(m+1)]
        results = list()
        for i in range(1, m+1):
            for j in range(1, n+1):
                pre[i][j] = pre[i-1][j] ^ pre[i][j-1] ^ pre[i-1][j-1] ^ matrix[i-1][j-1]
                results.append(pre[i][j])

        results.sort(reverse=True)
        return results[k-1]


if __name__ == '__main__':
    matrix = [[5,2], [1,6]]
    k = 3
    S = Solution()
    print(S.kthLargestValue(matrix, k))