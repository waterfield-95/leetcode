"""
2021.7
idea: string decode problem -> stack or recursion
1. stack: we need to decode string from inner to outer due to brackets
    - parse number: carry
    - parse string: alphabets
    - stack content: num, str, brackets(signs to push and pop element)

"""

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
                self.i += 1
                string = ''
                while stk[-1] != '[':
                    string = stk.pop() + string
                
                stk.pop()   # 弹出'['
                cur_num = stk.pop()
                new_string = string * cur_num
                stk.append(new_string)
            
        return ''.join(stk)

class Solution_recursion:
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

    def get_string(self):
        if self.i == self.n or self.s[self.i] == ']':
            return ''

        char_ = self.s[self.i]
        repeat_times = 0
        res = ''

        if char_.isdigit():
            repeat_times = self.parse_num()

            string_ = self.get_string()
            self.i += 1

            res += string_ * repeat_times
        
        elif char_.isalpha():
            res += char_
            self.i += 1
        
        return res + self.get_string()
        

    def decodeString(self, s: str) -> str:
        self.i = 0
        self.s = s
        self.n = len(self.s)

        return self.get_string()


class Solution:
    """
    2021.3
    assistant stack
    - parse number
    - parse alphabets
    - stk store (current layer string, next layer count) when it comes into '['
    - ']': stk pop -> get new string
    """
    def decodeString(self, s: str) -> str:
        string_ = ''
        next_count = 0
        stk = []

        for char_ in s:
            if char_.isdigit() == True:
                next_count = 10 * next_count + int(char_)
            elif char_.isalpa() == True:
                string_ += char_
            # push into stack
            elif char_ == '[':
                stk.append((string_, next_count))
                string_, next_count = '', 0
            # pop last layer elements
            elif char_ == ']':
                upper_string, count = stk.pop()
                string_ = upper_string + count * string_
        return string_


class Solution1:
    """
    DFS: 
        - base case: ']' -> return current idx and current string
        - recursive process: decode one layer content in the bracket
    """
    def decodeString(self, s: str)->str:
        def dfs(i):
            res, multiple = '', 0
            while i < len(s):
                if s[i].isdigit() == True:
                    multiple = 10 * multiple + int(s[i])
                
                elif s[i].isalpha() == True:
                    res += s[i]

                # start recursion
                elif s[i] == '[':
                    i, tmp = dfs(i+1)
                    res = res + multiple * tmp
                    multiple = 0
                    
                # complete recursion
                elif s[i] == ']':
                    return i, res

                else:
                    print('Something Wrong!')
                
                i += 1
            return res
        
        return dfs(0)


if __name__ == '__main__':
    s = "3[a]2[bc]"
    S = Solution_recursion()
    print(S.decodeString(s))
