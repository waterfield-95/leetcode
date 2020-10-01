‘’‘
date: 200926
idea: stack
’‘’

class Solution:
    def isValid(self, givenString: str) -> bool:
        params_dict = {')': '(', ']':'[', '}': '{'}
        stack = [];
        
        for character in givenString:
            if(character not in params_dict):
                stack.append(character);
            elif((stack) and (params_dict[character] == stack[-1])):
                stack.pop();
            else:
                return False;

        if(len(stack) == 0):
            return True;
        else: 
            return False;
