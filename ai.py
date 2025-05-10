from game_logic import drop_piece, get_next_available_row, valid_location


PLAYER_1 = 1
PLAYER_2 = 2
PLAYER_3 = 3

def minimax(board, depth, maximizing_player, alpha, beta):
    """
    Minimax algorithm with alpha-beta pruning.
    :param board: The current game board
    :param depth: Depth of the search tree
    :param maximizing_player: The player for whom we are maximizing the score
    :param alpha: Alpha value for pruning
    :param beta: Beta value for pruning
    :return: The best possible move for the current player
    """
    valid_moves = get_valid_moves(board)
    if depth == 0 or not valid_moves:
        return evaluate_board(board, maximizing_player)
    
    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        for move in valid_moves:
            temp_board = make_move(board, move, PLAYER_1) 
            eval = minimax(temp_board, depth - 1, False, alpha, beta)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in valid_moves:
            temp_board = make_move(board, move, PLAYER_2) 
            eval = minimax(temp_board, depth - 1, True, alpha, beta)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return best_move

def evaluate_board(board, maximizing_player):
    """
    A simple evaluation function for the board state.
    :param board: The current game board
    :param maximizing_player: The current player for whom we're evaluating the score
    :return: The evaluation score of the board
    """
    score = 0
    for r in range(6):
        for c in range(4):
            if all([board[r][c+i] == maximizing_player for i in range(4)]):
                score += 1
    for r in range(3):
        for c in range(7):
            if all([board[r+i][c] == maximizing_player for i in range(4)]):
                score += 1
    for r in range(3):
        for c in range(4):
            if all([board[r+i][c+i] == maximizing_player for i in range(4)]):
                score += 1
    for r in range(3, 6):
        for c in range(4):
            if all([board[r-i][c+i] == maximizing_player for i in range(4)]):
                score += 1
    return score

def get_valid_moves(board):
    valid_moves = []
    for c in range(7):
        if valid_location(board, c):
            valid_moves.append(c)
    return valid_moves

def make_move(board, col, piece):
    temp_board = [row.copy() for row in board] 
    row = get_next_available_row(temp_board, col)
    drop_piece(temp_board, row, col, piece)
    return temp_board
