from typing import List

class Vector2D:
    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.row = 0
        self.col = 0
        
    def check_and_modify(self):
        while self.row < len(self.vec) and self.col == len(self.vec[self.row]):
            self.row += 1
            self.col = 0

    def next(self) -> int:
        self.check_and_modify()
        result = self.vec[self.row][self.col]
        self.col += 1
        return result
        
    def hasNext(self) -> bool:
        self.check_and_modify()
        return self.row < len(self.vec)

class Vector2D_2:
    """
    bad design since we use extra space to construct a new list to store all elements
    """

    def __init__(self, vec: List[List[int]]):
        """
        O(N+V), N is number of input, V is number of empty inner list
        """
        self.flatten = []
        for row in range(len(vec)):
            for col in range(len(vec[row])):
                self.flatten.append(vec[row][col])
        
        self.next_ptr = 0
        

    def next(self) -> int:
        res = self.flatten[self.next_ptr]
        self.next_ptr += 1
        return res
    
    def hasNext(self) -> bool:
        return self.next_ptr < len(self.flatten)
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()