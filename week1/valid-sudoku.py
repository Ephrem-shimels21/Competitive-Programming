class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sub_board = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in sub_board[(i // 3, j // 3)]:
                    return False
                
                if board[i][j] != ".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    sub_board[(i // 3, j // 3)].add(board[i][j])
        return True
                

        