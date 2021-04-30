"""
2021.3
idea:
- Two stack are regarded as in_stack and out_stack, twice stack operation
"""

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_in = []
        self.stack_out = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_in.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack_out == []:
            while self.stack_in != []:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack_out == []:
            while self.stack_in != []:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.stack_out == [] and self.stack_in == []:
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
