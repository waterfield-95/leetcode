'''
date: 201010
idea:
1. recursion: calculate current row element through last one
2. iter
'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0: return [1]
        if rowIndex==1: return [1, 1]

        res = self.getRow(rowIndex-1)
        res = [1] + [ res[i] + res[i-1] for i in range(1, rowIndex)] + [1]

        return res
    
class Solution2:
    def getRow(rowIndex):
    # j行的数据, 应该由j - 1行的数据计算出来.
    # 假设j - 1行为[1,3,3,1], 那么我们前面插入一个0(j行的数据会比j-1行多一个),
    # 然后执行相加[0+1,1+3,3+3,3+1,1] = [1,4,6,4,1], 最后一个1保留即可.
    r = [1]
    for i in range(1, rowIndex + 1):
        r.insert(0, 0)
        # 因为i行的数据长度为i+1, 所以j+1不会越界, 并且最后一个1不会被修改.
        for j in range(i):
            r[j] = r[j] + r[j + 1]
    return r

"""
2011.2
idea:
3.calculate all elements with n rows
4. Rolling array: we use the last level numbers to calculate this layer number.
"""
class Solution3:
    def getRow(self, rowIndex):
        triangle = [1] * (rowIndex+1)
        for i in range(rowIndex+1):
            triangle[i] = [1] * (i+1)
            for j in range(1, i):
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
        return triangle[-1]
    
class Solution4:
    def getRow(self, rowIndex):
        # The first loop: traverse every layer
        for i in range(rowIndex+1):
            triangle = [1] * (i+1)
            # 2nd loop: in every layer, calculating every elements except the first and last one.
            for j in range(1, i):
                triangle[j] = pre[j-1] + pre[j]
            pre = triangle
        return triangle
