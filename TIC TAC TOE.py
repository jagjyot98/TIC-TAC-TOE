# board
# dsiplay board
# play game
# handle turn
# check win
# check rows
# check columns
# check diagonals
# check Tie
# flip PLAYER

# ------Global variable-------
game_going = True
winner = None
current_plr = "X"
board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]


def dsply_brd():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def ply_game():
    dsply_brd()

    while game_going:
        # handle arbitrary turns btw players
        handle_trn(current_plr)

        # check game ovr
        check_ovr()

        # flip to player
        flip_plr()

        # the game ended
    if winner == 'X' or winner == 'O':
        print(winner+" won.")
    elif winner is None:
        print("Tie.")


def handle_trn(player):
    # shows which player's turn is this
    print(player+"'s turn")

    position = input("choose a position from 1-9:")

    valid = False
    while not valid:
        # to check for correct input
        # continously asks for correct value
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9:")

        position = int(position) - 1

        if board[position] == "_":
            valid = True
        else:
            print("You can't go there.")

    board[position] = player
    dsply_brd()


def check_ovr():
    check_win()
    check_tie()


def check_win():
    # had to declare global here also to access it within any scope
    global winner
    # check rows
    row_winner = check_rows()
    # check columns
    col_winner = check_columns()
    # check diagonals
    dia_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif dia_winner:
        winner = dia_winner
    else:
        winner = None
    return


def check_rows():
    global game_going
    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"
    # if any row matches( will become True)
    # hence game over
    if row_1 or row_2 or row_3:
        game_going = False

    # what value won the game
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]


def check_columns():
    global game_going
    colm_1 = board[0] == board[3] == board[6] != "_"
    colm_2 = board[1] == board[4] == board[7] != "_"
    colm_3 = board[2] == board[5] == board[8] != "_"
    # if any column matches( will become True)
    # hence game over
    if colm_1 or colm_2 or colm_3:
        game_going = False

    # what value won the game
    if colm_1:
        return board[0]
    elif colm_2:
        return board[1]
    elif colm_3:
        return board[2]


def check_diagonals():
    global game_going
    dia_1 = board[0] == board[4] == board[8] != "_"
    dia_2 = board[2] == board[4] == board[6] != "_"
    # if any diagonal matches( will become True)
    # hence game over
    if dia_1 or dia_2:
        game_going = False

    # what value won the game
    if dia_1:
        return board[0]
    elif dia_2:
        return board[2]


def check_tie():
    global game_going
    if "_" not in board:
        game_going = False
    return


def flip_plr():
    global current_plr
    if current_plr == "X":
        current_plr = "O"
    elif current_plr == "O":
        current_plr = "X"
    return current_plr


ply_game()
