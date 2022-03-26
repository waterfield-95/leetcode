
class BitByBit:
    def reverseBits(self, n: int) -> int:
        ans, power = 0, 31
        while n:
            ans += (n & 1) << power
            n = n >> 1
            power -= 1
            
        return ans
        

class Self:
    def reverseBits(self, n: int) -> int:
        binary_str = format(n | 0x00000000, "b")
        binary_array = list(binary_str)
        k = 32 - len(binary_array)
        if k != 0:
            for i in range(k):
                binary_array.insert(0, "0")
        i, j = 0, len(binary_array) - 1
        while i < j:
            binary_array[i], binary_array[j] = binary_array[j], binary_array[i]
            i += 1
            j -= 1
        print(binary_array)
        return int("".join(binary_array), 2)
        
        