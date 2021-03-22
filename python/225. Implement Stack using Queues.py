"""
2021.3
idea:
- implement stack through two queue, which are data_queue and assistant_queue
"""

from collections import deque
 
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_queue = deque()
        self.assistant = deque()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.assistant.append(x)
        while self.data_queue:
            self.assistant.append(self.data_queue.popleft())
        self.data_queue, self.assistant = self.assistant, self.data_queue


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.data_queue.popleft()


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.data_queue[0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not bool(self.data_queue)



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
