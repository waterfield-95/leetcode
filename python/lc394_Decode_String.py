"""
2021.3
idea:
1. assistant stack
- digit as times_number, store times and existed_string into stack when it comes to '['; 
- ']' means pop current times and existed string from stack and then calculate current string;
- When it comes to 'char', update current string by appending char

2. DFS
- base case: 
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

class Solution1:
    def decodeString(self, s: str)->str:
        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i+1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res
        return dfs(s, 0)


# 2021.7 stack
class Solution_stack:
    def parse_num(self):
        num = 0
        while self.i < self.n and self.s[self.i].isdigit() == True:
            num = 10 * num + int(self.s[self.i])
            self.i += 1
        return num
            
    def parse_string(self):
        string = ''
        while self.i < self.n and self.s[self.i].isalpha() == True:
            string += self.s[self.i]
            self.i += 1
        return string

    def decodeString(self, s: str) -> str:
        self.i = 0
        self.s = s
        self.n = len(self.s)
        
        stk = []
        while self.i < self.n:
            if s[self.i].isdigit() == True:
                num = self.parse_num()
                stk.append(num)

            elif s[self.i].isalpha() == True:
                string = self.parse_string()
                stk.append(string)

            elif s[self.i] == '[':
                stk.append('[')
                self.i += 1
            
            elif s[self.i] == ']':
                #Fixme: cur_string need to be concatenated
                cur_string = stk.pop()
                if stk.pop() == '[':
                    print('Right')
                else:
                    print('Something Wrong!')
                cur_num = stk.pop()
                new_string = cur_string * cur_num
                stk.append(new_string)
        return stk[-1]
            


if __name__ == '__main__':
    s = '3[a2[c]]'
    S = Solution_stack()
    print(S.decodeString(s))
