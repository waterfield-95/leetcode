class Solution:
    """
    Tricky: n & (n-1) -> set the least significant 1-bit to 0
    """
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        
        while n != 0:
            cnt += 1
            n = n & (n-1)
        
        return cnt

class BitMask:
    def hammingWeight(self, n: int) -> int:
        mask = 1
        cnt = 0
        for i in range(32):
            if n & mask != 0:
                cnt += 1
            mask <<= 1
        return cnt

class Convert2str:
    def hammingWeight(self, n: int) -> int:
        binary_str = "{0:b}".format(n)
        cnt = 0
        for digit in binary_str:
            if digit == "1":
                cnt += 1
        
        return cnt
        
        