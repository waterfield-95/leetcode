from typing import List
import random


class Fisher_Yates:
    # Time: O(n), Space: O(n)
    # in-space element exchange 
    # by using decrement variable n which determine the offset of exchange position
    def __init__(self, nums: List[int]):
        self.array = nums
        self.original = nums.copy()

    def reset(self) -> List[int]:
        self.array = self.original  
        self.original = self.original.copy()
        return self.array

    def shuffle(self) -> List[int]:
        n = len(self.array)
        for i in range(n):
            change_offset = random.randrange(n)
            n -= 1
            self.array[i], self.array[i+change_offset] = self.array[i+change_offset], self.array[i]
        return self.array


class Solution:
    #TC: O(n^2)
    def __init__(self, nums: List[int]):
        self.array = nums
        self.original = nums.copy()  # clone

    def reset(self) -> List[int]:
        self.array = self.original
        self.original = self.original.copy()
        return self.array
        
    def shuffle(self) -> List[int]:
        aux = self.array.copy()
        for i in range(len(self.array)):
            rm_idx = random.randrange(len(aux))
            self.array[i] = aux.pop(rm_idx)
        return self.array

