"""
2021.4

idea: stack
- first add N to stack, and then judge the operator
- if operator is multiply or division, we need to calculator top number of stack and current number and then push result to stack
- if operator is addition, push current number to stack
- if operator is subtraction, multiply -1 and push to stack

Note python3 floor division is toward less value instead of zero like Cpp/Java, so we need to solve it through int(a/float(b))
"""

class Solution:
    def clumsy(self, N: int) -> int:
        stack = [N]
        index = 0
        for operand in range(N-1, 0, -1):
            if index == 0:
                stack.append(stack.pop() * operand)
            elif index == 1:
                stack.append(int(stack.pop()/float(operand)))
            elif index == 2:
                stack.append(operand)
            elif index == 3:
                stack.append(-1 * operand)
            index = (index+1) % 4
        return sum(stack)
