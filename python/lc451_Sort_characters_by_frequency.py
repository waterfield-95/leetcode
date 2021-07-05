"""
2021.7.3
idea: ordered dict by frequency and combine new string
"""

from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1
        
        freq_sort = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        res = ''
        for char, count in freq_sort:
            res += char*count
        return res


if __name__ == '__main__':
    s = 'tree'
    S = Solution()
    print(S.frequencySort(s))