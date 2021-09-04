class InvertToList:
    def reverse(self, x: int) -> int:
        BIGINT = 1 << 31
        sign = 1 if x >= 0 else -1
        result = 0
        while x:
            result = 10 * result + x % 10
            x //= 10
        
        result *= sign
        return result if result >= -BIGINT and result <= BIGINT-1 else 0

class Solution:
    def reverse(self, x: int) -> int:
        BIGINT = 1 << 31
        sign = 1 if x >= 0 else -1
        result = 0
        x = abs(x)
        while x:
            result = 10 * result + x % 10
            x //= 10
        
        result *= sign
        return result if result >= -BIGINT and result <= BIGINT-1 else 0


if __name__ == "__main__":
    'h'.isalnum()