from typing import List

class Solution:
    """
    Time: O(N*2^N)
    Space: O(N*2^N)
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        for i in range(2**n, 2**(n+1)):
            bitmasks = bin(i)[3:]
            
            result.append([ nums[j] for j in range(n) if bitmasks[j] == "1"])
        
        return result
            

class Backtrack:
    """
    Time: O(N*2^N)
    Space: O(N)
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first, path):
            if len(path) == k:
                result.append(path[:])
                return
            
            for i in range(first, n):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
        
        result = []
        n = len(nums)
        for k in range(n+1):
            backtrack(0, [])
        
        return result
        

class Cascade:
    """
    - To take each number into consideration for each time from the start of empty array []
    Time: O(2^N * N), there are 2^N possible result and then take N time to put them into result list
    Space: O(2^N * N)
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            for i in range(len(subsets)):
                subsets.append(subsets[i] + [num])
            
        
        return subsets

if __name__ == "__main__":
    nums = [1,2,3]
    S = Solution()
    print(S.subsets(nums))