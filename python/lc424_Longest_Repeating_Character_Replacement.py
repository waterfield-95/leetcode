"""
idea: slide window with two pointer
- set 26 char num list, each of them represents the number of the char in the current slide window
- set window_maxn as the char with max number in the current slide window
- move right and left pointer, and make the elements in the slide window satisfy "right-left+1 - window_maxn > k"
  - right-left+1 means the number of elements in the window
  - window_maxn means we need to minus the most element and thus leave substitute elements which must less than k. 
  - Otherwise, we need to move left pointer to reduce window size to satisfy the condition
  - At the end of s, right pointer points the next one of the last element, so we could return right-left/l-left, which represents the lenght of the slide window
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        num = [0] * 26
        window_maxn = left = right = 0
        l = len(s)
        while right < l:
            num[ord(s[right]) - ord('A')] += 1
            window_maxn = max(window_maxn, num[ord(s[right]) - ord('A')])
            if right - left + 1 - window_maxn > k:
                num[ord(s[left]) - ord('A')] -= 1
                left += 1
            right += 1
        
        return l - left
