def print_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_win(board, player):
    # Winning combinations (rows, columns, diagonals)
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combos)

def play_game():
    board = [" "] * 9
    current_player = "X"
    
    for turn in range(9):
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, choose a spot (1-9): ")) - 1
            if board[move] != " ":
                print("Spot taken! Try again.")
                continue
            board[move] = current_player
        except (ValueError, IndexError):
            print("Invalid input. Enter 1-9.")
            continue

        if check_win(board, current_player):
            print_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            return

        current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    play_game()

