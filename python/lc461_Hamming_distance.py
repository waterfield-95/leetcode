"""
2021.5
idea: 
    1. XOR, counting the number of 1 in the result
    
"""

class Solution:
    """
    would mask out the rest of the bits other than the rightmost bit
    """
    def hammingDistance(self, x: int, y: int) -> int:
        cnt = 0
        z = x ^ y
        mask = 1
        for i in range(32):
            if mask & z != 0:
                cnt += 1
            mask <<= 1
        return cnt
    
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
                
    