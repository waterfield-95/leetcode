"""
2021.2
idea:
1. double pointer to reverse list and inverse every elements
2. XOR, if row[i]==row[-1-i], inverse both, else nothing would happen
"""

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            for k in range(len(A)): row[k] = 1 - row[k]
            i, j = 0, len(row)-1
            while i < j:
                row[i], row[j] = row[j], row[i]
                i += 1
                j -= 1
        return A

class Solution2:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            for j in range((len(row) + 1) // 2):
                if row[j] == row[-1-j]:             # 采用Python化的符号索引
                    row[j] = row[-1-j] = 1 - row[j]    
        return A
