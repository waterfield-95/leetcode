"""
2021.4
idea: sort
1. string splicing for two number to get new string and then choose the larger one which the first number is larger than another.
2. Considering zero list, return result or '0'
"""

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key
        key = cmp_to_key(lambda x,y: int(x+y)-int(y+x))
        sorted_list = sorted(map(str, nums), key=key, reverse=True)
        result = ''.join(sorted_list).lstrip('0')
        return result or '0'
