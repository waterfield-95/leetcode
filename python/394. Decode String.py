"""
2021.3
idea:
1. assistant stack
- digit as times_number, store times and existed_string into stack when it comes to '['; 
- ']' means pop current times and existed string from stack and then calculate current string;
- When it comes to 'char', update current string by appending char

2. DFS
- recursive: base case
"""

class Solution:
    def decodeString(self, s: str) -> str:
        cur_string = ''
        times = 0
        stack = []
        for c in s:
            if '0' <= c <= '9':
                times = 10 * times + int(c)
            elif c == '[':
                stack.append([times, cur_string])
                times, cur_string = 0, ''
            elif c == ']':
                ctimes, existed_string = stack.pop()
                cur_string = existed_string + cur_string * ctimes
            else:
                cur_string += c
        return cur_string
