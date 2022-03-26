from typing import List

class Solution:
    """
    Time: O(log(MN))
    Space: O(1)
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        
        left, right = 0, n*m - 1
        while left <= right:
            mid = left + (right-left) // 2
            (i, j) = divmod(mid, m)
            if target == matrix[i][j]:
                return True
            else:
                if target < matrix[i][j]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return False
        