def domino_piling(board):
    board = board.split()
    board_size = int(board[0]) * int(board[1])
    
    max_domino = board_size // 2
    return max_domino

board = input()

print(domino_piling(board))