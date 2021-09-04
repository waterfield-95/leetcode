MAPPING = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

MAX_INT = (1 << 31) - 1
MIN_INT = - (1 << 31)

class Solution:
    def myAtoi(self, s: str) -> int:
        # ignore any leading whitespace
        s = s.lstrip()
        
        # check the sign
        sign = 1
        if len(s) > 0 and s[0] in ['-', '+']:
            if s[0] == '-':
                sign = -1
            s = s[1:]
        
        # check the digits
        num = 0
        for char in s:
            # char.isdigit()
            if char in MAPPING:
                num = num * 10 + MAPPING[char]
            else:
                break
                
        return self.clamping(sign*num)
        
    # clamp the integer result
    def clamping(self, num):
        if num < MIN_INT:
            num =  MIN_INT
        elif num > MAX_INT:
            num = MAX_INT
        return num
                
