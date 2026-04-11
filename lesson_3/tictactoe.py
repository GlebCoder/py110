import random
import os

VACANT = ' '
HUMAN_PLAYER = 'X'
COMPUTER_PLAYER = 'O'

def display_board(board):
    os.system('clear')
    print(f'You - {HUMAN_PLAYER}, Computer - {COMPUTER_PLAYER}')
    print(f'     |     |')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}  ')
    print(f'     |     |')
    print(f'-----*-----*-----')
    print(f'     |     |')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}  ')
    print(f'     |     |')
    print(f'-----*-----*-----')
    print(f'     |     |')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}  ')
    print(f'     |     |')

def initialize_board():
    return {number: ' ' for number in range(1, 10)}

def prompt(message):
    return f"==> {message}"

def get_valid_squares(board):
    return [key for key, value in board.items() if value == VACANT]

def player_chooses_square(board):
    valid_squares = [key for key, value in board.items() if value == VACANT]
    while True:
        print(prompt(f"Choose a square from {valid_squares}: "))
        square = int(input().strip())
        if square in valid_squares:
            break
        else:
            print(prompt(f"Invalid square number. You must choose from: {valid_squares}"))

    board[square] = HUMAN_PLAYER

def computer_chooses_square(board):
    valid_squares = get_valid_squares(board)
    if valid_squares:
        square = random.choice(valid_squares)
        board[square] = COMPUTER_PLAYER

def detect_winner(board):
    winning_combos = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7]
    ]
    for combo in winning_combos:
        key1, key2, key3 = combo
        if board[key1] == board[key2] == board[key3] == HUMAN_PLAYER:
            return "Player"
        elif board[key1] == board[key2] == board[key3] == COMPUTER_PLAYER:
            return "Computer"
    return None

def someone_won(board):
    return bool(detect_winner(board))

def board_full(board):
    return len(get_valid_squares(board)) == 0

while True:
    board = initialize_board()
    display_board(board)

    while True:
        player_chooses_square(board)
        display_board(board)
        if someone_won(board) or board_full(board):
            break

        computer_chooses_square(board)
        display_board(board)
        if someone_won(board) or board_full(board):
            break

    if someone_won(board):
        print(prompt(f"{detect_winner(board)} won!"))
    else:
        print(prompt("It's a tie"))

    print(prompt("Play again? y/n"))
    answer = input().strip().lower()
    if not answer or answer.strip()[0] != "y":
        break