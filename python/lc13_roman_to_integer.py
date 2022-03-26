"""
2021.5
idea: traverse string
    - if s[i] < s[i+1], we need to minus s[i] from the total sum
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }
        
        idx, n = 0, len(s)
        result = 0
        while idx < n:
            if idx + 1< n and s[idx:idx + 2] in d:
                result += d[s[idx:idx + 2]]
                idx += 2
            else:
                result += d[s[idx]]
                idx += 1
        
        return result

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        total = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and d[s[i]] < d[s[i+1]]:
                total += d[s[i+1]] - d[s[i]]
                i += 2
            else:
                total += d[s[i]]
                i += 1
                
        return total


if __name__ == '__main__':
    s = 'III'
    S = Solution()
    print(S.romanToInt(s))