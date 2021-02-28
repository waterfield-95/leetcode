"""
2021.2
idea: 
1. traverse twice and cmp sorted_list with origin_list
2. traverse once: judge two flags of non-inc and non-des
"""

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return sorted(A, reverse=True)==A or sorted(A) == A
      

class Solution2:
    def isMonotonic(self, A: List[int]) -> bool:
        inc, des = True, True
        n = len(A)
        for i in range(1, n):
            if A[i] > A[i-1]:
                des = False
            if A[i] < A[i-1]:
                inc = False
        return des or inc

# self programming at first time
class Solution3:
    def isMonotonic(self, A: List[int]) -> bool:
        flag = 0
        for i in range(1, len(A)):
            # 递减
            if A[i] < A[i-1]:
                if flag == 0:
                    flag = -1
                elif flag == 1:
                    return False
            # 递增
            elif A[i] > A[i-1]:
                if flag == 0:
                    flag = 1
                elif flag == -1:
                    return False
        return True
