"""
2021.7
Given two possible num array with the same length, n1, n2.
By replace one element by any other element in n1, return the minimum absolute sum difference between n1 and n2 index-wise
    - return sum(|replaced_n1[i] - n2[i]|)
    - min(|n1[i] - n2[i]| - |n1[j] - n2[i]|)
    - get max(|n1[j] - n2[i]|)
"""

from typing import List
import bisect

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        total = sum(abs(x-y) for x,y in zip(nums1, nums2))
        sn1 = sorted(nums1)
        best = 0
        for x,y in zip(nums1, nums2):
            cur = abs(x-y)
            # return left part of y in sn1 if y exists
            idx = bisect.bisect_left(sn1, y)    # idx might be n, because y might be larger than any elements in sn1
            # the first compute the maximum of best diff
            if idx < n:
                best = max(best, cur - (sn1[idx] - y))
            # if idx != 0, we need compute twice
            if idx > 0:
                best = max(best, cur - (y - sn1[idx-1]))
            
        return (total - best) % int(1e9+7)


if __name__ == '__main__':
    nums1 = [1,10,4,4,2,7]
    nums2 = [9,3,5,1,7,4]
    S = Solution()
    print(S.minAbsoluteSumDiff(nums1, nums2))
