class Solution:
    def countPrimes(self, n:int) -> int:
        # O(nloglogn) Eratosthenes
        prime_list = [i for i in range(n)]
        count = 0
        for i in range(2, n):
            if prime_list[i] != 0:
                count += 1
                if i*i < n:
                    for j in range(i*i, n, i):
                        prime_list[j] = 0
        return count

    def countPrimes_enumeration(self, n: int) -> int:
        def isPrime(x):
            for i in range(2, x):
                if x % i == 0:
                    return False
            return True
        
        if n < 3:
            return 0
        count = 0
        for i in range(2, n):
            if isPrime(i):
                count += 1
        return count

    def isUgly(self, n: int) -> bool:
        """
        traverse 2,3,5 as factor to be divided by n until the remainder is not equal to zero.
        """
        if n < 1:
            return False
        for factor in [2,3,5]:
            while n % factor == 0:
                n /= factor
        return n == 1

    def nthUglyNumber(self, n: int) -> int:
        import heapq
        heap = [1]
        seen = {1}
        for num in range(n):
            cur = heapq.heappop(heap)
            for factor in [2,3,5]:
                new = cur * factor
                if new not in seen:
                    heapq.heappush(heap, new)
                    seen.add(new)
        return cur
                

if __name__ == '__main__':
    n = 14   # true
    S = Solution()
    print(S.isUgly(1))