class MinStack1:
    """
    use tuple as one item to push into the top of underlying stack
    """
    def __init__(self):
        self.stack = list()
        
    def push(self, val: int) -> None:
        item = [val]
        if len(self.stack) == 0:
            self.stack.append([val, val])
        else:
            self.stack.append([val, min(self.stack[-1][1], val)])

    def pop(self) -> None:
        self.stack.pop(-1)
        
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


class MinStack2:
    """
    Two stack, if there is a minimum or equavalent minimum value, push it onto tracker
    """
    def __init__(self):
        self.stack = list()
        self.min_tracker_stack = list()

    def push(self, val: int) -> None:
        if len(self.stack) == 0 or val <= self.min_tracker_stack[-1]:
            self.min_tracker_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.min_tracker_stack[-1] == self.stack[-1]:
            self.min_tracker_stack.pop(-1)
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_tracker_stack[-1]
        

class MinStack_optimal:
    """
    Two stack with pair of current value and minimum stored in min_stack
    Reduce the times of repetitive of same minimum value
    """

    def __init__(self):
        self.stack = list()
        self.min_stack = list()
        
    def push(self, val: int) -> None:
        if not self.min_stack:
            self.min_stack.append([val, val])
        else:
            self.min_stack.append([val, min(val, self.min_stack[-1][1])])
        self.stack.append(val)
        
    def pop(self) -> None:
        if self.min_stack[-1][0] == self.stack[-1]:
            self.min_stack.pop(-1)
        
        self.stack.pop(-1)
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1][1]