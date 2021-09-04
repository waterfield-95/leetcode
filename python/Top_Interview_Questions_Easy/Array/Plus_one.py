from typing import List

class Convert2Num:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        num = 0
        for i in range(n):
            num += 10**(i) * digits[n-1-i]
        
        num += 1
        return [int(i) for i in str(num)]
        
class Recursion:
    """
    Optimal
    """
    def plusOne(self, digits):
        n = len(digits)
        if n == 1 and digits[0] == 9:
            digits = [1, 0]
            return digits

        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        if digits[-1] == 9:
            digits[-1] = 0
            digits = self.plusOne(digits[:-1]) + digits[-1:]
            return digits
        

if __name__  == '__main__':
    S = Recursion()
    digits = [9,9,9]
    print(S.plusOne(digits))
        