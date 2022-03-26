class New:
    """
    Time: O(N^2)
    Space: O(1)
    """
    def longestPalindrome(self, s: str) -> str:
        def expand_from_center(left, right, longest):
            while left >= 0 and right <= n - 1 and s[left] == s[right]:
                if right - left + 1 > longest[0]:
                    longest = right - left + 1, left, right
                left -= 1
                right += 1
            return longest
        
        # ans: length, left, right
        longest = 1, 0, 0
        n = len(s)
        for i in range(n):
            longest = expand_from_center(i, i, longest)
            longest = expand_from_center(i, i + 1, longest)

        return s[longest[1]:longest[2] + 1]



class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        if n < 1: return ""
        
        start, end = 0, 0   # inclusive
        for i in range(n):
            len1 = self.expandFromCenter(s, i, i)
            len2 = self.expandFromCenter(s, i, i+1)
            prev = end - start + 1
            l = max(len1, len2)
            if l > prev:
                start = i - (l-1) // 2
                end = i + l // 2
        
        return s[start:end+1]
        
    def expandFromCenter(self, s, left, right) -> int:  # return length
        while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
            left -= 1
            right += 1
            
        # left and right are exclusive
        return (right-1) - (left+1) + 1
        

class BruteForce:
    """
    Time limit Exceeded: O(n^3)
    """
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        for i in range(n):
            for j in range(i, n):
                cur = s[i:j+1]
                if self.isPalindrome(cur) and len(cur) > len(res):
                    res = cur       
        return res      
    
    def isPalindrome(self, s):
        left, right = 0, len(s)-1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -=1
            else:
                return False
        return True
        