from game_logic import create_board, valid_location, drop_piece, get_next_available_row, print_board, winning_move
from ai import minimax, evaluate_board, PLAYER_1, PLAYER_2, PLAYER_3

board = create_board()
game_over = False

current_player = PLAYER_1

print_board(board)

while not game_over:
    col = int(input(f"Player {current_player}, choose a column (0-6): "))

    if valid_location(board, col):
        row = get_next_available_row(board, col)
        drop_piece(board, row, col, current_player)

        print_board(board)

        if winning_move(board, current_player):
            print(f"Player {current_player} wins!")
            game_over = True
        else:
            if current_player == PLAYER_1:
                current_player = PLAYER_2
            elif current_player == PLAYER_2:
                current_player = PLAYER_3
            else:
                current_player = PLAYER_1
    else:
        print("Invalid move. Try again.")
