class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        O(n^2)
        """
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0
        left, right = 0, m
        while right < n+1:  
            if haystack[left:right] == needle:  # O(n)
                return left
            else:
                left += 1
                right += 1   
        return -1
        

if __name__ == '__main__':
    haystack = 'hello'
    needle = 'll'
    S = Solution()
    print(S.strStr(haystack, needle))