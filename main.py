from art import create_board, print_board
import random

board = create_board()

user_position = int(input("Please choose your input position:"))
user_choice = input("Please choose your choice: 'X' or 'O' ")

def is_valid_move(board, user_position):
    if user_position not in range(1, 10):
        return False
    if board[user_position] != " " :
        return False
    return True

def update_board(board, user_position, player):
    board[user_position] = player

def check_win(board):
    winning_combinations = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7)
    ]
    for a,b,c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None

winner = check_win(board)
if winner:
    print(f"Player {winner} wins!")
elif " " not in board.values():
    print("it's a draw!")
