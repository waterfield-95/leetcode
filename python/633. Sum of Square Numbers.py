"""
2021.4
idea: 
1. enumeration
  - enumrate each a, for i in range(int(sqrt(c)))
  - judge if there is a b to satisfy the condition
2. double pointer
  - set left, right pointer
  - According to the res which is equal to the sum of square of both of a and b, increment or decrement until left less than or equal to the right pointer
"""


import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        max_ = int(math.sqrt(c))
        for i in range(max_+1):
            another = math.sqrt(c - i**2)
            if another == int(another):
                return True
        return False

    def judgeSquareSum_2pointer(self, c):
        left = 0
        right = int(math.sqrt(c))
        while left <= right:
            res = left**2 + right**2
            if res == c:
                return True
            elif res > c:
                right -= 1
            else:
                left += 1
        return False

if __name__ == '__main__':
    c = 2
    S = Solution()
    # print(S.judgeSquareSum(c))
    print(S.judgeSquareSum_2pointer(c))
