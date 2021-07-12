"""
2021.7
idea
"""

from typing import List

class Solution:
    """
    O(n)
    """
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        n = len(citations)
        i = n-1
        while i >= 0 and citations[i] > h:
            h += 1
            i -= 1
        return  h


class Dichotomy:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        reverse_citations = citations[::-1]
        l, r = 0, n-1
        while l <= r:
            mid = l + r >> 1
            if reverse_citations[mid] >= mid + 1:
                l = mid + 1
            else:
                r = mid - 1
        return l


class Dichotomy2:
    """
    the maximum split point h:
        - citations[i] >= h, we need count into the right elements of x
        - discard the left elements
    
    Dichotomy:
    """
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n-1
        while l <= r:
            mid = l + (r - l) // 2
            if citations[mid] >= n - mid:
                r = mid - 1
            else:
                l = mid + 1
        return n - l


if __name__ == '__main__':
    citations = [0,1,3,5,6]
    S = Dichotomy()
    print(S.hIndex(citations))
