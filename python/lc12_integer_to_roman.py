"""
2021.5
idea: mapping roman symbols in 13 ways
    - greedy thinking: traverse, each time minus the biggest number until tmp is equal to 0
"""

class Solution:
     def intToRoman(self, num: int) -> str:
        roman_dict = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I',
        }
        
        sorted_tuple = sorted(roman_dict.items(), key=lambda x: x[0], reverse=True)
        
        roman_digits = []
        
        for value, roman in sorted_tuple:
            if num == 0: 
                break
            count, num = divmod(num, value)
            roman_digits.append(count * roman)
        
        return "".join(roman_digits)

    def intToRoman_hardcode(self,num):
        """
        硬编码，每一位可能的编码结果
        1 <= num <= 3999
        """
        THOUSANDS = ["", "M", "MM", "MMM"]
        HUNDREDS = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        TENS = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ONES = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        ans = THOUSANDS[num // 1000] + HUNDREDS[num % 1000 // 100] + \
                TENS[num % 100 // 10] + ONES[num % 10]
        return ans


if __name__ == '__main__':
    num = 140 # 'III'
    S = Solution()
    print(S.intToRoman_hardcode(num))
