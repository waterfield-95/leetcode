from typing import List

class Solution:
    """
    Time: O(N*3^L), L-> length of word
    Space: O(L) -> length of recursive stack
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        
        def backtrack(row, column, suffix):
            nonlocal board
            if not suffix:
                return True
            
            if row < 0 or row >=n or column<0 or column>=m or board[row][column] != suffix[0]:
                return False
            
            board[row][column] = "#"
            ret = False
            for row_offset, col_offset in [(1,0), (0,1), (-1,0), (0,-1)]:
                if backtrack(row+row_offset,  column+col_offset, suffix[1:]):
                    ret = True
            
            board[row][column] = suffix[0]
            return ret
            
            
            
        
        for i in range(n):
            for j in range(m):
                if backtrack(row=i, column=j, suffix=word):
                    return True
        
        return False
    
                