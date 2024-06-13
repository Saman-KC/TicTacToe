import random

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

total_score_p1 = 0
total_score_p2 = 0


def draw_board(board):
    print("  -----------")
    print(" | " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print("  -----------")
    print(" | " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print("  -----------")
    print(" | " + board[6] + " | " + board[7] + " | " + board[8] + " | ")
    print("  -----------")


def welcome(board):
    print("Welcome to TicTacToe")
    draw_board(board)


def get_player_move(board):
    try:
        pos = int(input("It's X turn! Choose a number between 1-9: "))
        while board[pos - 1] != " ":
            pos = int(input("Invalid space choose another space: "))
        pos = pos - 1
        board[pos] = "X"
    except:
        print("\nPlease choose a number between 1 - 9 only")
        draw_board(board)
        get_player_move(board)


def choose_p2_move(board):
    try:
        pos = int(input("It's O turn! Choose a number between 1-9: "))
        while board[pos - 1] != " ":
            pos = int(input("Invalid space choose another space: "))
        pos = pos - 1
        board[pos] = "O"
    except:
        print("\nPlease choose a number between 1 - 9 only")
        draw_board(board)
        get_player_move(board)


def check_for_win(board, mark):
    row1 = board[0] == board[1] == board[2] != " "
    row2 = board[3] == board[4] == board[5] != " "
    row3 = board[6] == board[7] == board[8] != " "
    col1 = board[0] == board[3] == board[6] != " "
    col2 = board[1] == board[4] == board[7] != " "
    col3 = board[2] == board[5] == board[8] != " "
    diag1 = board[0] == board[4] == board[8] != " "
    diag2 = board[6] == board[4] == board[2] != " "
    if row1 or row2 or row3 or col1 or col2 or col3 or diag1 or diag2:
        print(f"{mark} won\n")
        if mark == "X":
            return 1
        else:
            return -1
    return 0


def check_for_draw(board):
    i = 0
    count = 0
    for j in range(0, 8):
        if board[i + j] == " ":
            count = 1
    if count != 1:
        print("It's a draw!\n")
        return 0
    return 1


def play_game(board):
    draw_board(board)
    run = True
    while run:
        get_player_move(board)
        draw_board(board)
        if check_for_win(board, "X") == 1:
            return 1
            break
        if check_for_draw(board) == 0:
            return 0
            break
        choose_p2_move(board)
        draw_board(board)
        if check_for_win(board, "O") == -1:
            return -1
            break
        if check_for_draw(board) == 0:
            return 0
            break


def menu():
    global total_score_p1
    global total_score_p2
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    try:
        usr = int(input("""Enter choice: \n1) Play game \nq) Quit \n:"""))
        if usr == 1:
            va = play_game(board)
            if va == 1:
                total_score_p1 += 1
            elif va == -1:
                total_score_p2 += 1
            else:
                pass
            print("Your current score is:", total_score_p1, ":", total_score_p2)
        elif usr == "q":
            exit()
    except ValueError:
        print("Thanks for playing the game!")
        exit()


while True:
    menu()
