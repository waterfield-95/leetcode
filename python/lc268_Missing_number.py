from typing import List

class BruteForce:
    def missingNumber(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        expected = len(sorted_nums)
        print(sorted_nums)
        for i, num in enumerate(sorted_nums):
            if i != num:
                expected = i
                break
        return expected
                
class Hashset:
    def missingNumber(self, nums: List[int]) -> int:
        hashset = set(nums)
        for i in range(len(nums)+1):
            if i not in hashset:
                return i
        
            
        