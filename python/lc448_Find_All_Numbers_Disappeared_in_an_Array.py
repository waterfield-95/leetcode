"""
2021.2
idea: 
1. set subtraction due to the deduplication of a set
2. In place: by add n to each value as index, nums[(value-1)%n] += n, and then traverse nums and get elements which are less than or equal to n.
- index: [0,n-1], representing this element of index whether or not is the  disappeared value according to its value(<=n)
- value: [1,n], if the value is larger than n, its index representing the lack of number which is not add to n need to be put in result list and return.
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res_set = set(i for i in range(1, n+1))
        nums_set = set(nums)
        return res_set - nums_set
    
class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums:
            x = (num - 1) % n
            nums[x] += n
        
        res = []
        for i, num in enumerate(nums):
            if num <= n:
                res.append(i+1)
        return res
