"""
2021.5
idea: brute force
    - a^b=c -> c^a=b, c^b=a
"""

from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = []
        arr.append(first)
        for i in range(len(encoded)):
            arr.append(arr[i] ^ encoded[i])
        return arr