"""
2021.7
idea: Given sorted citations array to compute h-Index
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
            # mid and left part are satisfied
            if reverse_citations[mid] >= mid + 1:
                l = mid + 1
            else:
                r = mid - 1
        # l=r+1
        # current l is boundary which is not satisfied with condition
        # because it represents the index, so the number of the first l index is l+1
        # so the boundary which is satisfied with the condition is l+1-1=l
        return l    


class Dichotomy2:
    """
    the maximum split point h:
        - citations[i] >= h, we need count into the right elements of x
        - discard the left elements
    
    Dichotomy: boundary condition
        - To ensure the minimum citations (mid) are larger than the number of papers (n-mid)
        which means, the right part of mid are all satisfied
        - r is not necessarily satisfied, while l must be satifsfied, so return n-l
    """
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n-1
        while l <= r:
            mid = l + (r - l) // 2
            # condition boundary -> mid and the right part are satisfied with condition
            if citations[mid] >= n - mid:
                r = mid - 1
            else:
                l = mid + 1
        return n - l


if __name__ == '__main__':
    citations = [0,1,3,5,6]
    S = Dichotomy2()
    print(S.hIndex(citations))
