"""
2021.5
idea: 
    1. XOR, counting the number of 1 in the result
    
"""

class Solution:
    def hammingDistance_self(self, x: int, y: int) -> int:
        def convert2bin32(x):
            return ''.join(['0' if c==' ' else c for c in '{:32b}'.format(x)])
        x_bin = convert2bin32(x)
        y_bin = convert2bin32(y)
        c = 0
        for i in range(32):
            if x_bin[i] != y_bin[i]:
                c += 1
        return c
    
    def numberof1_1(self, n):
        return bin(n & 0xffffffff).count('1')   # 与全1按位与为了保证负数的正常表示

    def numberof1_2(self, n):
        n_bin = n & 0xffffffff
        temp = 0x00000001
        c = 0
        for i in range(32):
            if (n_bin & temp) != 0:
                c += 1
            temp = temp << 1
        return c

    def hammingDistance_XOR(self, x, y):
        res = x^y
        return self.numberof1_2(res)


if __name__ == '__main__':
    n = -1
    x, y = 10223, 301
    S = Solution()
    print(S.hammingDistance_self(x, y), S.hammingDistance_XOR(x,y))
                
    