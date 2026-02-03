from art import create_board, print_board
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *


root = tk.Tk()
root.title("TicTacToe")

board = create_board()
current_player = "X"
game_over = False

def is_valid_move(board, pos):
    return pos in range(1, 10) and board[pos] == " "

def update_board(board, pos, player):
    board[pos] = player

def check_win(board):
    wins = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7)
    ]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None

def is_draw(board):
    return " " not in board.values()

root = tk.Tk()
root.title("Tic Tac Toe")

status = tk.Label(root, text = f"Player {current_player}'s turn", font=("Arial", 14))
status.grid(row=0, column=0, columnspan=3, pady=8)

buttons = {}

def set_all_buttons_state(state):
    for b in buttons.values():
        b.config(state = state)

def on_click(pos):
    global current_player, game_over

    if game_over:
        return

    if not is_valid_move(board, pos):
        status.config(text = "Cell already taken. Choose another.")

    #apply move in board
    update_board(board, pos, current_player)
    buttons[pos].config(text=current_player, state="disabled")

    #check win/draw
    winner = check_win(board)
    if winner:
        status.config(text=f"Player {winner} wins!")
        game_over = True
        set_all_buttons_state("disabled")
        return

    if is_draw(board):
        status.config(text="It's a draw!")
        game_over = True
        set_all_buttons_state("disabled")
        return

    #switch player
    current_player = "O" if current_player == "X" else "X"
    status.config(text = f"Player {current_player}'s turn")

def reset_game():
    global board, current_player, game_over
    board = create_board()
    current_player = "X"
    game_over = False
    status.config(text=f"{current_player}'s turn")
    for pos in range(1,10):
        buttons[pos].config(text=" ", state = "normal")

#create 3x3 grid of buttons
for pos in range(1, 10):
    r = 1 + (pos - 1) // 3
    c = (pos - 1) % 3
    btn = tk.Button(
        root,
        text = " ",
        width= 6,
        height= 3,
        font= ("Arial", 18),
        command=lambda p=pos: on_click(p),
    )
    btn.grid(row=r, column=c, padx=4, pady=4)
    buttons[pos] = btn

reset_btn = tk.Button(root, text="Reset", command= reset_game)
reset_btn.grid(row= 4, column= 0, columnspan= 3, sticky= "we", pady= (6, 10))

root.mainloop()