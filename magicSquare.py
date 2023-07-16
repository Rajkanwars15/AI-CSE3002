import numpy as np
import random

# Define the magic square constants
magic_constants = {
    3: 15,
    4: 34,
    5: 65,
    6: 111,
    7: 175,
    8: 260
}

# Set up the game board as a matrix
board = np.full((3, 3), '-')

# Define a function to print the game board
def print_board():
    for row in board:
        print(' | '.join(row))

# Define a function to handle the user's turn
def user_turn():
    print("Your turn.")
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
    board[row][col] = "X"
    print_board()

# Define a function to check if the game is over
def check_game_over():
    # Check for a win
    for row in board:
        if "-" not in row and np.sum([int(cell) if cell.isdigit() else 0 for cell in row]) == magic_constants[3]:
            return "win"
    for col in range(3):
        if "-" not in board[:, col] and np.sum([int(cell) if cell.isdigit() else 0 for cell in board[:, col]]) == magic_constants[3]:
            return "win"
    if "-" not in np.diag(board) and np.sum([int(cell) if cell.isdigit() else 0 for cell in np.diag(board)]) == magic_constants[3]:
        return "win"
    if "-" not in np.diag(np.fliplr(board)) and np.sum([int(cell) if cell.isdigit() else 0 for cell in np.diag(np.fliplr(board))]) == magic_constants[3]:
        return "win"
    # Check for a tie
    elif "-" not in board:
        return "tie"
    # Game is not over
    else:
        return "play"

# Define the computer's turn using a random move
def computer_turn():
    print("Computer's turn.")
    available_positions = np.argwhere(board == "-")
    position = random.choice(available_positions)
    board[position[0]][position[1]] = "O"
    print_board()

# Define the main game loop
def play_game():
    print("Tic-Tac-Toe: User versus Computer")
    print_board()
    game_over = False
    while not game_over:
        user_turn()
        game_result = check_game_over()
        if game_result == "win":
            print("You win!")
            game_over = True
        elif game_result == "tie":
            print("It's a tie!")
            game_over = True
        else:
            computer_turn()
            game_result = check_game_over()
            if game_result == "win":
                print("Computer wins!")
                game_over = True
            elif game_result == "tie":
                print("It's a tie!")
                game_over = True

# Start the game
play_game()
