"""
2021.6.29
idea: 26-binary form transformation (1,26), not (0, 25), so We need to minus 1 to get difference with 'A'
    - calculate remainder to determine UPPERCASE alphabet
    - calculate quotient to do next iteration

"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # unicode 'A' -> 65
        res = []
        def dfs(num):
            nonlocal res
            if num == 0:
                return
            num -= 1
            res.append(chr(ord('A') + num % 26))
            dfs(num//26)

        dfs(columnNumber)
        return ''.join(res[::-1])


class Solution2:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = list()
        while columnNumber > 0:
            a0 = (columnNumber - 1) % 26 + 1
            ans.append(chr(a0 - 1 + ord("A")))
            columnNumber = (columnNumber - a0) // 26    # a0 might be 26
        return "".join(ans[::-1])


class Solution3:
    def convertToTitle(self, columnNumber):
        ans = list()
        while columnNumber > 0:
            columnNumber -= 1
            ans.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26
        return ''.join(ans[::-1])


if __name__ == '__main__':
    columnNumber = 1520
    S = Solution()
    print(S.convertToTitle(columnNumber))
