"""
2021.5
idea:
1. stack
"""

class Solution:
    def reverseParentheses_stack(self, s: str) -> str:
        stack = []
        str_ = ''
        for char in s:
            if char == '(':
                stack.append(str_)
                str_ = ''
            elif char == ')':
                str_ = stack.pop() + str_[::-1]
            else:
                str_ += char
        return str_

    def reverseParentheses_recursion(self, s):
        s = list(s)
        def dfs(s):
            ans = ''
            while len(s) != 0:
                c = s.pop(0)
                if c == '(':
                    ans += dfs(s)
                if c not in '()':
                    ans += c
                if c == ')':
                    return ans[::-1]
            return ans
        return dfs(s)
                    

if __name__ == '__main__':
    s = 'a(u(love)i)b'
    S = Solution()
    print(S.reverseParentheses_stack(s))
    print(S.reverseParentheses_recursion(s))
