class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        p1 = p2 = 0
        while p1 <= (len(haystack) - len(needle)):
            for i in range(len(needle)):
                if haystack[p2] == needle[i]:
                    p2 += 1
                    if i == len(needle)-1:
                        return p1
                else:
                    break
            p2 = p1 = p1 + 1
        return -1

    def strStr_bf(self, haystack, needle):
        if needle == '':
            return 0
        n = len(haystack)
        m = len(needle)
        flag = -1
        for i in range(n-m+1):
            for j in range(m):
                if haystack[i+j] != needle[j]:
                    break
                elif j == m-1:
                    return i
        return -1
                    

if __name__ == '__main__':
    haystack = 'abbaa'
    needle = 'bba'
    S = Solution()
    print(S.strStr_bf(haystack, needle))