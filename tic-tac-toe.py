# Tic Tac Toe Game in Python

# Display the board
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Check if there's a win
def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Check if board is full (draw)
def check_draw(board):
    return all([cell != " " for row in board for cell in row])

# Main game loop
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        display_board(board)
        
        # Player input
        try:
            row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
            col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        
        # Check if the move is valid
        if row in range(3) and col in range(3) and board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Invalid move, try again.")
            continue
        
        # Check win or draw
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            display_board(board)
            print("It's a draw!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()
