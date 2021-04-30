'''
date: 200927
idea: Monotonic stack, ensure the following number is less than the previous one
- Using M-stack to store index of temperature and traverse list
- while-loop for the stack, and if the new temperature is more than the temperature of the top number of stack, calculate the difference to push into answer list
'''

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = list()
        ans = [0 for i in range(len(T))]
        for i, temp in enumerate(T):
            while stack and temp > T[stack[-1]]:
                prev_index =  stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans
                
