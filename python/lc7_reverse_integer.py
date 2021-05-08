"""
2021.5
idea: mod and floor divide
    - python3: -3//10=-1, -3%10=7
    - modified:
        - floor divide -3//10+1=0
        - mod: if x<0 and digit>0: digit= x%10-10
"""


class Solution:
    def reverse(self, x):
        # -2147483648, 2147483647
        INT_MIN, INT_MAX = -2**31, 2**31-1
        rev = 0
        while x != 0:
            # python3 向下取整，rev<-214748364
            if rev < INT_MIN//10 + 1 or rev > INT_MAX//10:
                return 0
            digit = x % 10
            # python3 取模运算在负数时，由于余数是向下取整，所以模是[0,9)正数
            # digit -10%10=0
            if x < 0 and digit > 0:
                digit -= 10
            # python3 取余时向下取整，不能写为 x=x//10，否则负数有影响
            x = (x-digit) // 10
            rev = rev * 10 + digit
        return rev

    def reverse1(self, x):
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        rev = 0
        while x != 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10
        

    def reverse_imperfect(self, x: int) -> int:
        n = len(x)
        ans = 0
        s = str(x)
        if s[0] == '-':
            ans = -1 * int(self.reverse_string(s[1:]))
        else:
            ans = int(self.reverse_string(s))

        if ans > (2**31-1) or ans < -2**31:
            return 0
        return ans

    def reverse_string(self, s):
        left, right = 0, len(s)-1
        sl = list(s)
        while left < right:
            sl[left], sl[right] = sl[right], sl[left]
            left += 1
            right -= 1
        return ''.join(sl)
        

if __name__ == '__main__':
    x1 = 123    # 321
    x2 = -123
    x3 = 120
    x4 = 1534236469
    S = Solution()
    print(S.reverse(x1))
    print(S.reverse(x2))
    print(S.reverse(x3))
    print(S.reverse(x4))
