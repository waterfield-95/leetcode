from typing import List
from functools import lru_cache

"""
This problem contains 0 in array, so some position cannot jump to the end of array
"""

class Optimal:
    """
    Time: O(N)
    Space: O(1)
    """
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 0:
            return True

        last_pos = n - 1
        for cur in range(n-2, -1, -1):
            if cur + nums[cur] >= last_pos:
                last_pos = cur
            
        return last_pos == 0
            
# Test: [2,3,1,1,4]
            

class DP_TopDown:
    """
    Sometime it can be accepted
    """
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        @lru_cache(None)
        def dp(i):
            if i == n - 1:
                return True
            
            for j in range(i+1, min(i+nums[i], n-1) + 1):
                if dp(j):
                    return True
            return False
        
        return dp(0)

class RecursiveMem:
    """
    Time limited exceeded, while Java with same method can be accepted
    """
    def __init__(self) -> None:
        self.mem = {}
    def canJump(self, nums: List[int]) -> bool:
        self.mem[len(nums)-1] = True
        return self.canJumpFromPosition(0, nums)
    
    def canJumpFromPosition(self, pos, nums):   # jump to end
        if pos in self.mem:
            return self.mem[pos]

        jump_furthest = min(pos + nums[pos], len(nums)-1)
        for next_pos in range(jump_furthest, pos, -1):
            if self.canJumpFromPosition(next_pos, nums):
                self.mem[pos] = True
                return True
        
        self.mem[pos] = False
        return False

class DP_BottomUp:
    """
    O(n^2)
    """
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        canJumpFromList = [False for _ in range(n)]
        canJumpFromList[n-1] = True
        for i in range(n-2, -1, -1):
            furthest_idx = min(i+nums[i], n-1)
            for j in range(i+1, furthest_idx+1):
                if canJumpFromList[j]:
                    canJumpFromList[i] = True
                    break
        return canJumpFromList[0]
        

if __name__ == "__main__":
    nums1 = [2,3,1,1,4]  # true
    nums2 = [3,2,1,0,4] # false
    S = Solution()
    print(S.canJump(nums1))
    # print(S.canJump(nums2))
