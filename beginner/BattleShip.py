__author__ = 'galo javier'

from random import randint

board = []
ship_size = 1


def create_board():
    for x in range(5):
        board.append(["O"] * 5)


def print_board():
    for row in board:
        print(" ".join(row))


def random_row():
    return randint(0, len(board) - 1)


def random_col():
    return randint(0, len(board[0]) - 1)


def rematch():
    board.clear()
    create_board()


def init_game(multiplayer):
    rematch_flag = True

    while rematch_flag:
        print("Let's play Battleship!")
        create_board()
        print_board()
        random_row()
        random_col()

        ship_row = random_row()
        ship_col = random_col()

        print(ship_row)
        print(ship_col)

        turns = 4
        player_one_turn = True

        if multiplayer:
            turns = 6

        for turn in range(turns-1):

            if player_one_turn:
                print("Player 1")
            else:
                print("Player 2")

            guess_row = int(input("Guess Row:"))
            guess_col = int(input("Guess Col:"))

            if guess_row == ship_row and guess_col == ship_col:
                print("Congratulations! You sunk my battleship!")
                if player_one_turn:
                    print("Player 1")
                else:
                    print("Player 2")
                break
            else:
                if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                    print("Oops, that's not even in the ocean.")
                elif "X" == board[guess_row][guess_col]:
                    print("You guessed that one already.")
                else:
                    print("You missed my battleship!")
                    board[guess_row][guess_col] = "X"
                print("Turn", turn + 1)
                print_board()
                if multiplayer:
                    player_one_turn = not player_one_turn

        print("Game Over")
        rematch_flag = bool(input("Rematch Y/N") == "Y")
        if rematch_flag:
           rematch()


multiplayer_param = bool(input("multiplayer?")=="Y")
print("Multi ", multiplayer_param)
init_game(multiplayer_param)