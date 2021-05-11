"""
2021.5
idea: XOR skill
    - calculate the first element in permutation list: perm[0] = total_xor ^ except_1_xor
    - traverse to calculate each element through the principle of XOR reversal properties
        - x ^ y = z
        - z ^ x = y
        - z ^ y = x
"""

from typing import List
from operator import xor
from functools import reduce

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded)
        except_xor = 0
        total_xor = 0
        for i in range(1, n+2):
            total_xor ^= i
        for j in range(1, n, 2):
            except_xor ^= encoded[j]
        
        perm = [0] * (n+1)
        perm[0] = total_xor ^ except_xor
        for i in range(1, n+1):
            perm[i] = encoded[i-1] ^ perm[i-1]
        return perm

    def decode_official(self, encoded):
        n = len(encoded)
        total = reduce(xor, range(1, n+2))
        odd = 0
        for i in range(1, n, 2):
            odd ^= encoded[i]

        # the first element
        perm = [total ^ odd]
        for i in range(n):
            perm.append(perm[-1] ^ encoded[i])
        return perm


if __name__ == '__main__':
    encoded = [3,1] # [1,2,3]
    S = Solution()
    print(S.decode_official(encoded))
    