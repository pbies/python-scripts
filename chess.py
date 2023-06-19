#!/usr/bin/env python3

# Chessboard
board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

# Function to display the chessboard
def display_board(board):
    for row in board:
        print(' '.join(row))
    print()

# Function to check if a move is valid
def is_valid_move(start, end):
    start_row, start_col = start
    end_row, end_col = end
    piece = board[start_row][start_col]

    # Check if the start position contains a piece
    if piece == '.':
        return False

    # Check if the end position is within the board boundaries
    if end_row < 0 or end_row > 7 or end_col < 0 or end_col > 7:
        return False

    # Check if the move is valid for the piece
    # (This is a simplified implementation without considering piece-specific rules)
    return True

# Function to make a move
def make_move(start, end):
    start_row, start_col = start
    end_row, end_col = end
    piece = board[start_row][start_col]

    # Make the move by updating the board
    board[start_row][start_col] = '.'
    board[end_row][end_col] = piece

# Game loop
current_player = 1  # Player 1 starts
while True:
    display_board(board)

    # Get the move from the current player
    if current_player == 1:
        print("Player 1's turn")
    else:
        print("Player 2's turn")

    start_row = int(input("Enter the start row (0-7): "))
    start_col = int(input("Enter the start column (0-7): "))
    end_row = int(input("Enter the end row (0-7): "))
    end_col = int(input("Enter the end column (0-7): "))

    start = (start_row, start_col)
    end = (end_row, end_col)

    # Check if the move is valid
    if is_valid_move(start, end):
        make_move(start, end)
        current_player = 2 if current_player == 1 else 1
    else:
        print("Invalid move. Try again.")
    
    print()
