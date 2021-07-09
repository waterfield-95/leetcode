"""
2021.7
idea: moore vote algo. -> to find the mode in the array.
    - While there might not be mode in the array, we need judge the number of candidate in the end
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = -1
        count = 0
        for num in nums:
            if count <= 0:
                candidate = num
                count = 0
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        cnt = 0
        for num in nums:
            if num == candidate:
                cnt += 1

        return candidate if cnt*2 > len(nums) else -1
            


if __name__ == '__main__':
    nums = [1,2,5,9,5,9,5,5,5]
    S = Solution()
    print(S.majorityElement(nums))