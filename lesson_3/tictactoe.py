import random
import os

VACANT = ' '
HUMAN_PLAYER = 'X'
COMPUTER_PLAYER = 'O'
NUMBER_OF_GAMES = 5
WINNING_COMBOS = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
]
YES = ['y', 'ye', 'yes', 'yep']
NO = ['n', 'no', 'not', 'nope']


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
    return [str(key) for key, value in board.items() if value == VACANT]

def join_or(lst, sep=', ', last_sep='or'):
    if len(lst) == 0:
        return ''
    if len(lst) == 1:
        return lst[0]
    if len(lst) == 2:
        return f"{lst[0]} {last_sep} {lst[1]}"
    last_square = lst[-1]
    new_lst = lst[:-1] + [last_sep]
    new_lst_str = sep.join(new_lst)
    return f'{new_lst_str} {last_square}'

def player_chooses_square(board):
    valid_squares = get_valid_squares(board)
    while True:
        valid_choice = join_or(valid_squares)
        print(prompt(f"Choose a square {valid_choice}:"))
        square = input().strip()
        if square in valid_squares:
            break
        else:
            print(prompt(f"Invalid square number. You must choose: {valid_choice}"))

    board[int(square)] = HUMAN_PLAYER

def square_at_risk(line, board):
    choices = [board[key] for key in line]
    if choices.count(HUMAN_PLAYER) == 2:
        for key in line:
            if board[key] == VACANT:
                return key
    return None

def square_to_attack(line, board):
    choices = [board[key] for key in line]
    if choices.count(COMPUTER_PLAYER) == 2:
        for key in line:
            if board[key] == VACANT:
                return key
    return None


def computer_chooses_square(board):
    for combo in WINNING_COMBOS:
        square_to_win = square_to_attack(combo, board)
        if square_to_win:
            board[square_to_win] = COMPUTER_PLAYER
            return

    for combo in WINNING_COMBOS:
        square = square_at_risk(combo, board)
        if square:
            board[square] = COMPUTER_PLAYER
            return

    if board[5] == VACANT:
        board[5] = COMPUTER_PLAYER
        return

    valid_squares = get_valid_squares(board)
    if valid_squares:
        square = random.choice(valid_squares)
        board[int(square)] = COMPUTER_PLAYER

def choose_square(board, player):
    if player == "1":
        player_chooses_square(board)
    else:
        computer_chooses_square(board)

def change_player(player):
    if player == "1":
        player = "2"
    else:
        player = "1"
    return player

def detect_winner(board):
    for combo in WINNING_COMBOS:
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

def display_match_result(player, computer):
    if player > computer:
        print(prompt("Player won the match"))
    elif player < computer:
        print(prompt("Computer won the match"))
    else:
        print(prompt("Match is over. It's a tie"))

player_win = 0
computer_win = 0
count = 0
while True:
    board = initialize_board()
    while True:
        player = input(prompt("Choose who moves first: 1 - you, 2 - computer: ")).strip().casefold()
        if player in ("1", "2"):
            break
        else:
            print(prompt("Invalid input. Try again."))

    display_board(board)

    while True:
        choose_square(board, player)
        display_board(board)
        player = change_player(player)
        if someone_won(board) or board_full(board):
            break

    if someone_won(board):
        winner = detect_winner(board)
        print(prompt(f"{winner} won!"))
    else:
        winner = None
        print(prompt("It's a tie"))

    input(prompt("Enter any key to continue..."))

    count += 1
    if winner == "Player":
        player_win += 1
    if winner == "Computer":
        computer_win += 1

    print(prompt(f"Player won {player_win} times and computer won {computer_win} times"))

    if count == NUMBER_OF_GAMES:
        display_match_result(player_win, computer_win)
        print(prompt("Play another match? y/n"))
        answer = input().strip().lower()

        while answer not in NO and answer not in YES:
            print(prompt("Invalid answer. Try again."))
            print(prompt("Play another match? y/n"))
            answer = input().strip().lower()

        if answer in NO:
            break

        count = 0
        player_win = 0
        computer_win = 0