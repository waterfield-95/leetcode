"""
idea: reverse insertion 
- double pointer to point the last of element in the nums1 and nums2, the 3rd pointer to represent the element which is about to insert
- compare and insert, in the end, add the rest of elements in nums2 to the head of nums1 (Merge elements in s2 to s1)
"""
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr = m + n - 1
        i, j = m - 1, n - 1
        while i >= 0 and j >= 0:
            if nums2[j] >= nums1[i]:
                nums1[ptr] = nums2[j]
                j -= 1
            else:
                nums1[ptr] = nums1[i]
                i -= 1
            ptr -= 1
        if j >= 0:
            nums1[:ptr + 1] = nums2[:j + 1]
# Time: O(m + n)
# Space: O(1)

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # two get pointers for nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        # set pointer for nums1
        p = m + n - 1
        while p >= 0 and p2 >= 0:
            if p1 < 0:
                nums1[p] = nums2[p2]
                p2 -= 1
                p -= 1
                continue
            if nums2[p2] > nums1[p1]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        
        # add rest elem in nums2 to nums1
        nums1[:p2+1] = nums2[:p2+1]
