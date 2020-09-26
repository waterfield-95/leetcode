‘’‘
date: 200926
idea: stack
’‘’

class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')': '(', ']':'[', '}': '{'}
        st = [];
        
        for c in s:
            if(c not in dic):
                st.append(c);
            elif(st and dic[c] == st[-1]):
                st.pop();
            else:
                return False;

        if(len(st) == 0):
            return True;
        else: return False;
