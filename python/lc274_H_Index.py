"""
2021.7
idea: Given the citations array to compute H-index 
(the maximum h number of papers with at least h citations)
    - H-index = max(#papers equal to or larger than certain citations, the citations)
"""

from typing import List

class Solution:
    """
    sort and traverse
    Time: O(nlogn) sort
    Space: O(n) n-array
    """
    def hIndex(self, citations: List[int]) -> int:
        sorted_citation = sorted(citations, reverse = True)
        h = 0; i = 0; n = len(citations)
        while i < n and sorted_citation[i] > h:
            h += 1
            i += 1
        return h


class Optimal:
    """
    To reduce the time complexity of sorting, we use counter array
    - index: number of citations, if larger than n, count into n. 
        - reseacher A has 10 papers, one of which has 100 citations.
    - value: the number of satisfied paper
    - Traverse n positive integer in reverse order:
        - count total number of papers
        - if total is larger than number of papers, return them

    - Time: O(n)
    """
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        total = 0   # number of satisfied papers
        counter = [0] * (n+1)
        # counter to record paper counts equal to or larger than n, index represents citations
        for num in citations:
            # if citations larger than n, count into n
            if num >= n:
                counter[n] += 1
            else:
                counter[num] += 1
        
        # traverse paper number in reverse order
        for i in range(n, -1, -1):
            total += counter[i]
            # judge by number of papers with proper citations
            if total >= i:
                return i
        return 0


class Dichotomy:
    """
    hIndex satisfied the duality on the positive integer axis: the maximum value x
        - the value less than or equal to x must satisfied condition
        - larger value does not satisfied the condition

    Time complexity: O(NlogN)
    
    """
    def check(self, citations, mid) -> bool:
        """
        check whether mid value satisfied hIndex condition
        """
        cnt = 0
        for val in citations:
            if val >= mid:  # mid serve as citation value
                cnt += 1
        
        if cnt >= mid:  # mid serve as paper number
            return True
        else:
            return False


    def hIndex(self, citations):
        n = len(citations)
        l, r = 0, n
        while l <= r:
            mid = l + r >> 1
            if self.check(citations, mid):
                l = mid + 1
            else:
                r = mid - 1
        return r

        


if __name__ == '__main__':
    citations = [0]
    S = Optimal()
    print(S.hIndex(citations))
    
