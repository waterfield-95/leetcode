"""
idea: hash to calculate two-sum question
"""


class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        for i, a in enumerate(A):
            for j, b in enumerate(B):
                sum_A = sum(A) - a + b 
                sum_B = sum(B) - b + a 
                if sum_A == sum_B:
                    return [a, b]
