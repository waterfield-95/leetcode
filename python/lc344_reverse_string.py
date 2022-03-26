"""
2021.5
idea: double pointer
"""

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        Space: O(n) -> recursive stack
        """
        
        def helper(left, right):
            if left >= right:
                return
            s[left], s[right] = s[right], s[left]
            helper(left+1, right-1)
        
        helper(0, len(s)-1)
        return s
                