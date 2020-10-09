'''
date: 201009
idea: iteration
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for row in range(numRows):
            row_list = [None for _ in range(row+1)]
            row_list[0], row_list[-1] = 1, 1

            if len(row_list)>2:
                for col in range(1, len(row_list)-1):
                    row_list[col] = triangle[row-1][col-1] + triangle[row-1][col]

            triangle.append(row_list)
        return triangle          
