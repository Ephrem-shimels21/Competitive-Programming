# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # m = len(board)
        # n = len(board[0])

        # def is_bounded(row, col):
        #     return 0 <= row < len(board) and 0 <= col < len(board[0])

        # def is_border(row, col):
        #     direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        #     res = True
        #     for ofx, ofy in direction:
        #         res and not is_bounded(row + ofx, col + ofy)
            
        #     return res
        
        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] == "O" and is_border:
        #             board[i][j] = "."
        
        # for i in range(m):
        #     for j in range()

        def dfs(i: int, j: int) -> None:
            board[i][j] = '.'  
            directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]  
          
            for direction in directions:
                x, y = i + direction[0], j + direction[1]
                if 0 <= x < rows and 0 <= y < cols and board[x][y] == 'O':
                    dfs(x, y)
      
        rows, cols = len(board), len(board[0])
      
        for i in range(rows):
            for j in range(cols):
                is_border_cell = i in (0, rows - 1) or j in (0, cols - 1)
                if board[i][j] == 'O' and is_border_cell:
                    dfs(i, j)
      
       
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '.':
                    board[i][j] = 'O'


