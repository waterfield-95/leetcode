class Recursive:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        
        if n % 3 != 0 or n == 0:
            return False
        else:
            return self.isPowerOfThree(n/3)
        
class Iteration:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n < 1:
            return False
        
        while n % 3 == 0:
            n /= 3
        
        return n == 1