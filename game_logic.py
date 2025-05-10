def create_board():
    return [[0 for _ in range(7)] for _ in range(6)]

def valid_location(board, col):
    return board[0][col] == 0

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def get_next_available_row(board, col):
    for row in range(5, -1, -1):
        if board[row][col] == 0:
            return row

def print_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))
    print("\n")

def winning_move(board, piece):
    for r in range(6):
        for c in range(4):
            if all([board[r][c+i] == piece for i in range(4)]):
                return True
    for r in range(3):
        for c in range(7):
            if all([board[r+i][c] == piece for i in range(4)]):
                return True
    for r in range(3):
        for c in range(4):
            if all([board[r+i][c+i] == piece for i in range(4)]):
                return True
    for r in range(3, 6):
        for c in range(4):
            if all([board[r-i][c+i] == piece for i in range(4)]):
                return True

    return False
