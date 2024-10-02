# Tic-Tac-Toe game

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if there's a winner
def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # Horizontal
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), # Vertical
                      (0, 4, 8), (2, 4, 6)]            # Diagonal
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full
def check_full(board):
    return ' ' not in board

# Function to play the game
def play_game():
    board = [' '] * 9
    current_player = 'X'
    
    while True:
        print_board(board)
        
        try:
            move = int(input(f"Player {current_player}, choose your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = current_player
            else:
                print("This spot is already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if check_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()