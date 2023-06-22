import numpy as np

# Set up the game board as a matrix
board = np.full((3, 3), '-')

# Define a function to print the game board
def print_board():
    for row in board:
        print(' | '.join(row))

# Define a function to handle a player's turn
def take_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Choose a valid input from 1-9: ")
    position = int(position) - 1
    row = position // 3
    col = position % 3
    while board[row][col] != "-":
        position = int(input("Position already taken. Choose a different position: ")) - 1
        row = position // 3
        col = position % 3
    board[row][col] = player
    print_board()

# Define a function to check if the game is over
def check_game_over():
    # Check for a win
    for row in board:
        if row[0] == row[1] == row[2] != "-":
            return "win"
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "-":
            return "win"
    if (board[0][0] == board[1][1] == board[2][2] != "-") or \
       (board[0][2] == board[1][1] == board[2][0] != "-"):
        return "win"
    # Check for a tie
    elif "-" not in board:
        return "tie"
    # Game is not over
    else:
        return "play"

# Define the main game loop
def play_game():
    print_board()
    current_player = "X"
    game_over = False
    while not game_over:
        take_turn(current_player)
        game_result = check_game_over()
        if game_result == "win":
            print(current_player + " wins!")
            game_over = True
        elif game_result == "tie":
            print("It's a tie!")
            game_over = True
        else:
            # Switch to the other player
            current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()
