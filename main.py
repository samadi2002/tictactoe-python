from art import print_board
import random


board = [i for i in range(9)]
print_board(board)

user_position = int(input("Please choose your input position:"))
user_choice = input("Please choose your choice: 'X' or 'O' ")

def update_board(user_position, user_choice):

