"""
2021.2
idea: hashtable {num: [counts, left, right]}
- Then, traverse the hash value (list), get the minimum length which is the maximum counts in the nums
- Notice the situation that there are same maximum counts condition
"""


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count_dict = {}
        for i in range(len(nums)):
            if nums[i] in count_dict.keys():
                count_dict[nums[i]][0] += 1
                count_dict[nums[i]][2] = i
            else:
                count_dict[nums[i]] = [1, i, i]
        
        max_count = 0
        min_len = 50000
        for count, left, right in count_dict.values():
            if max_count < count:
                max_count = count
                min_len = right - left + 1
            elif max_count == count:
                if min_len > right - left + 1:
                    min_len = right - left + 1
        return min_len
                    
            
            
