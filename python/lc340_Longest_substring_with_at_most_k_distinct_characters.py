class Optimal:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        window = dict()
        left = 0
        
        for right in range(n):
            window[s[right]] = right
            if len(window) > k:
                leftmost_idx = min(window.values())
                del window[s[leftmost_idx]]
                left = leftmost_idx + 1
            
            ans = max(ans, right - left + 1)
        
        return ans
    # Time: O(n), n = len(s)
    # Space: O(k)
    
class Solution:
    """
    Time: O(nk)
    Space: O(k)
    """
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        def number_of_char(window):
            cnt = 0
            for key, val in window.items():
                if val != 0:
                    cnt += 1
            return cnt        
        
        n = len(s)
        ans = 0
        window = collections.Counter()
        left = 0
        
        for right in range(n):
            window[s[right]] += 1
            while left <= right and number_of_char(window) > k:
                window[s[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans