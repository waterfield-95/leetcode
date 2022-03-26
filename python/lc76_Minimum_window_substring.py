import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_cnts = collections.Counter(t)
        window_cnts = collections.Counter()
        left = 0
        formed = 0
        ans = float("inf"), None, None
        
        for right in range(len(s)):
            c = s[right]
            window_cnts[c] = window_cnts.get(c, 0) + 1
            if window_cnts[c] == t_cnts[c]:
                formed += 1
            
            while left <= right and formed == len(t_cnts):
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1), left, right
                c =s[left]
                window_cnts[c] -= 1
                if window_cnts[c] < t_cnts[c]:
                    formed -= 1
                left += 1
                
        
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]        
        
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = collections.Counter(t)
        if not s or not t:
            return ""
        
        s_dict = collections.Counter(s)
        for c in t_dict:
            if c not in s_dict or t_dict[c] > s_dict[c]:
                return ""
        
        min_window = s
        
        
        n = len(s)
        left = 0
        cnt = 0
        
        window_dict = dict()
        for right in range(n):
            if s[right] in t_dict:
                window_dict[s[right]] = window_dict.get(s[right], 0) + 1
                if window_dict[s[right]] == t_dict[s[right]]:
                    cnt += 1
            
            while left <= right and cnt == len(t_dict):
                if right - left + 1 < len(min_window):
                    min_window = s[left:right + 1]
                
                if s[left] in window_dict:
                    window_dict[s[left]] -= 1
                    if window_dict[s[left]] < t_dict[s[left]]:
                        cnt -= 1
                left += 1
        
        return min_window
            
        