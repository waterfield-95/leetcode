'''
date: 200926
idea: stack
'''

class Optimal:
    def isValid(self, s: str) -> bool:
        map = { ")": "(", "]": "[", "}":"{"}
        
        stack = []
        
        for c in s:
            if c in map:
                top = stack.pop() if stack else "#"
                if top != map[c]:
                    return False
                
            else:
                stack.append(c)
        
        return not stack

class Solution:
    """
    2021.12
    """
    def isValid(self, s: str) -> bool:
        map = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        
        stack = []
        for c in s:
            if c in map.keys():
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop(-1)
                if c != map[top]:
                    return False
        
        return not stack
        
                

class Solution:
    def isValid(self, givenString: str) -> bool:
        params_dict = {')': '(', ']':'[', '}': '{'}
        stack = []
        
        for character in givenString:
            if(character not in params_dict):
                stack.append(character)
            elif((stack) and (params_dict[character] == stack[-1])):
                stack.pop()
            else:
                return False

        if(len(stack) == 0):
            return True
        else: 
            return False
