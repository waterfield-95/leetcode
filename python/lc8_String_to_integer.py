class Solution:
    """
    Note: 
    - clarification: cosidering all the conner cases
    - Know how to clamp integer range by just comparing INT_MAX
    """
    def myAtoi(self, s: str) -> int:
        INT_MAX = (1 << 31) - 1
        INT_MIN = - (1 << 31)
        
        sign = 1
        idx = 0
        n = len(s)
        
        # delete leading space
        while idx < n and s[idx] == " ":
            idx += 1
        
        # check flag
        if idx < n and s[idx] == "+":
            sign = 1
            idx += 1
        elif idx < n and s[idx] == "-":
            sign = -1
            idx += 1
        
        # convert character to digit
        result = 0
        while idx < n and s[idx].isdigit():
            digit = int(s[idx])
            if (result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN
            else:
                result = result * 10 + digit
                idx += 1
        
        return sign * result
        