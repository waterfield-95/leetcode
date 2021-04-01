'''
date: 200927

What's Reverse Polish Notation?
- the operator follows their operands: 先写数字，后面跟着操作符号
- Advantage: removes the need for parentheses 

idea: stack to store number
- when encountering a number, push it to the stack
- when encounteringn a operator, take out the top two numbers of the stack for calculation, and push the result into the stack
'''

class Solution:
    def evalRPN(self, tokens) -> int:
        stack = list()
        oper = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }
        for token in tokens:
            if token not in oper:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                temp = int(oper[token](op1, op2))
                stack.append(temp)

        return stack[-1]
