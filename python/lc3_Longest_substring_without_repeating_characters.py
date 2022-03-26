class Optimal:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        window = dict()
        left = 0
        ans = 0
        
        for right in range(n):
            if s[right] in window:
                left = max(left, window[s[right]] + 1)
            
            window[s[right]] = right
            ans = max(ans, right - left + 1)
        return ans
            

class SlideWindow:

    """
    Time complexity: O(2n)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        n = len(s)

        window = set()
        ans = 0
        while right < n:
            if s[right] not in window:
                ans = max(ans, right - left + 1)
                window.add(s[right])
            else:
                while s[left] != s[right]:
                    window.remove(s[left])
                    left += 1
                left += 1
            
            right += 1
        return ans

    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        n = len(s)
        window = set()
        ans = 0
        
        for right in range(n):
            while left < n and s[right] in window:
                window.remove(s[left])
                left += 1
            
            ans = max(ans, right - left + 1)
            window.add(s[right])
        
        return ans

    def lengthOfLongestSubstring(self, s: str) -> int:
        # directed access table, ASCII characters number: 128
        chars = [0] * 128
        
        left = right = 0
        n = len(s)
        res = 0
        
        while right < n:
            # extend the window
            r_char = s[right]
            chars[ord(r_char)] += 1
            
            # extract the window
            while chars[ord(r_char)] > 1:
                l_char = s[left]
                chars[ord(l_char)] -= 1
                left += 1
                
            
            res = max(res, right - left + 1)
            right += 1
        
        return res

class BruteForce:
    """
    Time complexity: O(n^3), Limited Time Exceed
    Space: O(A) A-> 128
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check(start, end, s):
            chars = [0] * 128
            for i in range(start, end+1):
                c = s[i]
                chars[ord(c)] += 1
                if chars[ord(c)] > 1:
                    return False
            return True
        
        n = len(s)
        res = 0 
        for i in range(n):
            for j in range(i, n):
                if check(i, j, s):
                    res = max(res, j-i+1)
        return res


if __name__ == "__main__":
    s = "abcabcbb"  #3
    S = BruteForce()
    print(S.lengthOfLongestSubstring(s))