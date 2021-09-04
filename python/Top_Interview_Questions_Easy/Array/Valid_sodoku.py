from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = set()
            column = set()
            for j in range(9):
                if board[i][j] in row or board[j][i] in column:
                    return False
                else:
                    if board[i][j] != '.':
                        row.add(board[i][j])
                    
                    if board[j][i] != '.':
                        column.add(board[j][i])
                        
        # check sub-boxes of grid
        check = [[] for _ in range(9)]
        c = -3
        for i in range(9):
            if i % 3 == 0:
                c += 3
            for j in range(9):
                idx = c + j // 3
                for elem in check[idx]:
                    if board[i][j] == elem:
                        return False
                if board[i][j] != '.':
                    check[idx].append(board[i][j])
        
        return True


class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        rows = [set() for _ in range(n)]
        columns = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                num = board[i][j]
                if num == '.':
                    continue
                
                if num in rows[i]:
                    return False
                else:
                    rows[i].add(num)
                
                if num in columns[j]:
                    return False
                else:
                    columns[j].add(num)
                
                idx = i // 3 * 3 + j // 3
                if num in boxes[idx]:
                    return False
                else:
                    boxes[idx].add(num)
        return True

class Optimal:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Optimal, bitmasking
        """
        n = len(board)
        rows = [0] * n
        columns = [0] * n
        boxes = [0] * n
        
        for i in range(n):
            for j in range(n):
                val = board[i][j]
                if val == '.':
                    continue
                
                # keep consistant with idx of array
                pos = int(val) - 1
                
                if rows[i] & (1 << pos):    # if shows before
                    return False
                else:
                    rows[i] |= (1 << pos)
                    
                if columns[j] & (1 << pos):
                    return False
                else:
                    columns[j] |= (1 << pos)
                
                idx = i // 3 * 3 + j // 3
                if boxes[idx] & (1 << pos):
                    return False
                else:
                    boxes[idx] |= (1 << pos) 
        return True

                
if __name__ == '__main__':
    board = [
        ["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    S = Solution2()
    print(S.isValidSudoku(board))