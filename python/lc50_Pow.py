class Optimal:
    """
    T: O(logN)
    S: O(1)
    """
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
            
        res = 1
        while n > 0:
            if n % 2 == 1:  # when bit of binary representation is equal to 1
                res *= x    
            x *= x  # calculate x^1, x^2, x^4, x^8 -> binary representation, "10"->b"1010"
            n //= 2
        return res

class Solution:
    """
    Time: O(logN)
    Space: O(logN) -> recursive stack
    """
    def myPow(self, x: float, n: int) -> float:
        # 2^10 <- 2^5 * 2^5 <- 2^2*2^2*2
        def log_pow(x, n):
            if n == 0:
                return 1
            half_pow = log_pow(x, n // 2)
            if n % 2 == 1:
                return half_pow * half_pow * x
            else:
                return half_pow * half_pow
            
        if n < 0:
            x = 1 / x
            n = -n
        
        return log_pow(x, n)

