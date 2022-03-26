from typing import List

'''
date: 201009
idea: DP
'''

class Optimal:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for row_num in range(1, numRows):
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1
            for i in range(1, row_num):
                row[i] = ans[-1][i-1] + ans[-1][i]
            ans.append(row)
        return ans
    
class Solution2:
    triangle = []
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0: return []
        if numRows==1: return [[1]]

        triangle = self.generate(numRows-1)
        triangle.append([1] + [triangle[-1][i-1] + triangle[-1][i] for i in range(1, numRows-1)] + [1])

        return triangle
