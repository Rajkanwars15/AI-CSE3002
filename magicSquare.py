import numpy as np

# Set up the game board as a matrix (3x3 size) initialized with empty strings
board = np.full((3, 3), '', dtype=str)

# Define a function to print the game board
def print_board():
    for row in board:
        print(' | '.join(row))

# Define a function to handle a player's turn
def take_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")  # prompt for position
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:  # only choose 1-9
        position = input("Choose a valid input from 1-9: ")
    position = int(position) - 1  # str to int. -1 since index starts at 0
    row = position // 3  # int div- 0, 1, 2; eg (9 - 1 //3 = 3) = 2
    col = position % 3  # modulo- 0, 1, 2
    while board[row][col] != '':
        position = int(input("Position already taken. Choose a different position: ")) - 1
        row = position // 3  # int div- 0, 1, 2; eg (9  -1 //3 = 3) = 2
        col = position % 3  # modulo- 0, 1, 2
    board[row][col] = player
    print_board()

# Define a function to check if the game is over
def check_game_over():
    # Check for a win
    for row in board:
        if row[0] == row[1] == row[2] != '':
            return "win"
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return "win"
    if board[0][0] == board[1][1] == board[2][2] != '' or board[0][2] == board[1][1] == board[2][0] != '':
        return "win"
    # Check for a tie
    if '' not in board:
        return "tie"
    # Game is not over
    return "play"

# Define the main game loop
def play_game():
    print_board()
    current_player = "X"
    game_over = False
    while not game_over:
        if current_player == "X":
            take_turn(current_player)
        else:
            # Computer's turn
            available_positions = np.where(board == '')
            if len(available_positions[0]) > 0:
                # Check if the computer can win in the next move
                for i in range(len(available_positions[0])):
                    row, col = available_positions[0][i], available_positions[1][i]
                    board[row][col] = current_player
                    if check_game_over() == "win":
                        game_over = True
                        break
                    else:
                        board[row][col] = ''
                if not game_over:
                    # If computer cannot win, choose a random available position
                    position_index = np.random.choice(len(available_positions[0]))
                    row, col = available_positions[0][position_index], available_positions[1][position_index]
                    board[row][col] = current_player

        print_board()
        game_result = check_game_over()
        if game_result == "win":
            print(current_player + " wins!")
            game_over = True
        elif game_result == "tie":
            print("It's a tie!")
            game_over = True

        # Switch to the other player
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()
