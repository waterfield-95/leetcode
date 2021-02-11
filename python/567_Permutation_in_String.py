"""

"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        for char in s1:
            if char in s1_dict.keys():
                s1_dict[char] += 1
            else:
                s1_dict[char] = 1
        
        
        left, right = 0, 0
        n = len(s2)
        count_dict = {}
        while right < n:
            if s2[right] in s1_dict.keys():
                count = count_dict.setdefault(s2[right], 0)
                count_dict[s2[right]] = count + 1
                
                if count_dict == s1_dict:
                    return True

                if count_dict[s2[right]] > s1_dict[s2[right]]:
                    count_dict[s2[left]] -= 1
                    left += 1
                    right += 1
                    continue
                else:
                    right += 1
            
            else:
                count_dict = {}
                left = right = right + 1
        
        return False
