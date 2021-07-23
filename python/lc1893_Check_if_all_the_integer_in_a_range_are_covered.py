"""
2021.7
Given 2D array ranges and boundary: left and right.

"""

from typing import List

class Solution:
    """
    counts the number of the integer apperance in the ranges
    - Time: O(n^2+l)
    - Space: O(l)
    """
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # index as integer between 1-50
        counts = [0] * 51
        for start, end in ranges:
            for i in range(start, end+1):
                counts[i] += 1
        
        for i in range(left, right+1):
            if counts[i] == 0:
                return False
        return True

class Diff:
    """
    - diff array: the amount of change in the number of covered interval between two adjacent integers 
    - prefix sum: traverse from the beginning and accumulate to get index counts
    - Time: O(n+l), Space: O(l)
    """
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0] * 52 # diff array
        for l, r in ranges:
            diff[l] += 1
            diff[r+1] -=1 
        
        # prefix sum
        curr = 0
        for i in range(1, 51):
            curr += diff[i]
            if left <= i <= right and curr <= 0:
                return False
        return True


if __name__ == '__main__':
    ranges = [[1,2], [3,4], [5,6]]
    left = 2
    right = 5
    S = Solution()
    print(S.isCovered(ranges, left, right))
