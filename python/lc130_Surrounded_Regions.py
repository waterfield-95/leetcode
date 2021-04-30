"""
2021.3
idea:
1. BFS:
- add all boarder nodes to unchanged_deque because they aren't captured by Xs
- traverse neighbors of every node with 4 neighbors in the 2-dimension array until queue is empty. If the node's neighbor is 'O', add to deque. Remember to change traversed node to another char, or it would affect result of neighbor node
- traverse all node, keep unchanged node as 'O', the rest of nodes are assigned to 'X' 
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        unchanged = collections.deque()
        for i in range(m):
            if board[i][0] == 'O':
                unchanged.append((i, 0))
            if board[i][n-1] == 'O':
                unchanged.append((i, n-1))
        for j in range(n):
            if board[0][j] == 'O':
                unchanged.append((0,j))
            if board[m-1][j] == 'O':
                unchanged.append((m-1, j))
        
        while unchanged:
            x, y = unchanged.popleft()
            board[x][y] = 'A'
            for i, j in [(x+1,y), (x,y+1), (x-1,y), (x, y-1)]:
                if 0<=i<m and 0<=j<n and board[i][j]=='O':
                    unchanged.append((i,j))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
                    
