"""
2021.6.29
idea: iteration, Twenty-six binary count
    - given a string in Twenty-six binary form to calculate decimal number
    - from the end to beginning, 26**i * (current char number in decimal) and count sum
"""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for i in range(len(columnTitle)):
            res += 26**i * (ord(columnTitle[::-1][i]) - ord('A') + 1)
        return res


class Solution2:
    def titleToNumber(self, columnTitle):
        number, multiple = 0, 1
        for i in range(len(columnTitle)-1, -1, -1):
            k = ord(columnTitle[i]) - ord('A') + 1
            number += k * multiple
            multiple *= 26
        return number


if __name__ == '__main__':
    columnTitle = 'AB'
    S = Solution()
    print(S.titleToNumber(columnTitle))
    