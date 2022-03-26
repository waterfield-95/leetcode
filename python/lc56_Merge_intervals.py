from typing import List

class Solution:
    """
    Time: O(NlogN)
    Space: O(N) to store result, O(logN) for quicksort through recursion
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        res = []
        
        for i in range(len(intervals)):
            if i == 0 or intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])
        
        # Time: O(nlogn)
        # Space: O(n)
        return res

