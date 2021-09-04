from typing import List

class HorizontalScan:
    """
    Horizontal scan
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            s = strs[i]
            j = 0
            boundary = min(len(prefix), len(s))
            while j < boundary:
                if s[j] == prefix[j]:
                    j += 1
                else:
                    break
            prefix = s[:j]

            if prefix == '':
                return ''

        return prefix

class VerticalScan:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        # i: index of char in a string
        for i in range(len(strs[0])):
            char = strs[0][i]
            # j: index of string in the array of string
            for j in range(1, len(strs)):
                if len(strs[j]) == i or strs[j][i] != char:
                    return strs[0][:i]

        return strs[0]


if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    S = VerticalScan()
    print(S.longestCommonPrefix(strs))
