from typing import List

class TwoPassHash:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        d = {}
        for i, num in enumerate(nums):
            d[target - num] = i
        
        for i in range(n):
            if nums[i] in d and d[nums[i]] != i:
                return [i, d[nums[i]]]
        

class OnePass:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        hashtable = dict()
        for i, num in enumerate(nums):
            if (target - num) in hashtable:
                return [hashtable[target - num], i]
            hashtable[num] = i
