'''
date: 201010
idea:
1. recursion: calculate current row element through last one
'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0: return [1]
        if rowIndex==1: return [1, 1]

        res = self.getRow(rowIndex-1)
        res = [1] + [ res[i] + res[i-1] for i in range(1, rowIndex)] + [1]

        return res
