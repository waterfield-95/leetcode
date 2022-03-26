from typing import List

class Solution:
    """
    Time: O(n)
    Space: O(n)
    """
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        prev = lower - 1
        for i in range(len(nums)+1):
            if i == len(nums):
                cur = upper + 1
            else:
                cur = nums[i]
            
            if prev+1 <= cur-1:
                res.append(self.formatRange(prev+1, cur-1))
            prev = cur
                
        return res
        
    
    def formatRange(self, l, r):
        if l == r:
            return str(l)
        else:
            return f"{l}->{r}"