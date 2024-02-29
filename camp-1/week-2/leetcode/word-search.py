class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        def find_word(i, j, idx):
            if idx == len(word) - 1:
                return board[i][j] == word[idx]

            if board[i][j] != word[idx]:
                return False
            
            c = board[i][j]
            board[i][j] = "0"
            for x, y in pairwise((-1,0,1,0,-1)):
                new_x, new_y = i + x, y + j

                if 0 <= new_x < rows and 0 <= new_y < cols and board[new_x][new_y] != "0":
                    if find_word(new_x, new_y, idx + 1):
                        return True
            board[i][j] = c
            return False
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and find_word(i,j,0):
                    return True
        return False


           


            

