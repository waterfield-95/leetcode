"""
idea: slide window with fixed width
 - two dict, respectively, record the number of occurrence in s1 and slide window (solve elements out of order)
 - right boundary: traverse from index of len(s1) - 1 in s2
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        for char in s1:
            if char in s1_dict.keys():
                s1_dict[char] += 1
            else:
                s1_dict[char] = 1
        
        left, right = 0, len(s1)-1
        n = len(s2)
        window_dict = {}
        for char in s2[left:right]:
            count = window_dict.setdefault(char, 0)
            window_dict[char] = count + 1

        while right < n:
            c = window_dict.setdefault(s2[right], 0)
            window_dict[s2[right]] = c + 1
            if window_dict == s1_dict:
                return True
            else:
                window_dict[s2[left]] -= 1
                if window_dict[s2[left]] == 0:
                    del window_dict[s2[left]]
                left += 1
                right += 1

        return False
