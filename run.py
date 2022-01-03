# feature for computer choose to randomly.
from random import randint


def set_board_size():
    """
    The user chooses size of the gaming board.
    """
    size = []
    valid = False
    while valid is not True:
        try:
            board_size = int(input(
                "How big would you like the sea? (2 - 10): "))
            if board_size < 2:
                print("Too smal, enter a number between 2 - 10")
            elif board_size > 10:
                print("Too large, enter a number between 2 - 10")
            else:
                for _ in range(board_size):
                    size.append(["O"] * board_size)
                valid = True
        except ValueError:
            print("Not a number, try again")
        return size


def user_ships(size):
    """
    User input coordinates for where he/she would like to place
    their ship.
    """
    valid_row = False
    valid_col = False
    print(("Where do you what to place your ships? Enter a number between 1 - {} ").format(len(size)))
    while valid_row is not True:
        try:
            user_row = int(input("Enter row for your ship: "))
            if user_row not in range(1, len(size) + 1):
                print("Not valid row, enter a number 1 - {}".format(len(size) + 1))
            else:
                valid_row = True
        except ValueError:
            print("Not a number, try again")
    while valid_col is not True:
        try:
            user_row = int(input("Enter column for your ship: "))
            if user_row not in range(1, len(size) + 1):
                print("Not valid column, enter a number 1 - {}".format(len(size) + 1))
            else:
                valid_col = True
        except ValueError:
            print("Not a number, try again")
    return size


def random_row(size):
    """
    Function to be used in comp_shop and find_ship to find a random row
    """
    return randint(0, len(size) - 1)


def random_col(size):
    """
    Function to be used in comp_shop and find_ship to find a random column
    """
    return randint(0, len(size) - 1)


def find_ship(size):
    """
    Computer chooses a hidden ship location 
    away from user ship location.
    """
    valid_enemy_location = False
    while valid_enemy_location is not True:
        enemy_row = random_row(size)
        enemy_col = random_col(size)
        if size[enemy_row][enemy_col] != "#":
            return enemy_row, enemy_col


def print_board(size):
    """
    Print out the board.
    """
    for row in size:
        print(("   ").join(row))
    print(" ")


def row_guess(size):
    """
    Row coordinates for players shot.
    """
    valid_row = False
    print("Enter a number between 1 - {}".format(len(size)))
    while valid_row is not True:
        try:
            guess_row = int(input("Guess row: "))
            if guess_row not in range(1, len(size) + 1):
                print("Not a valid row, enter a number between 1 - {}".format(len(size)))
            else:
                valid_row = True
        except ValueError:
            print("Not a number, try again")
    return guess_row - 1


def col_guess(size):
    """
    Column coordinates for players shot.
    """
    valid_col = False
    print("Enter a number between 1 - {}".format(len(size)))
    while valid_col is not True:
        try:
            guess_col = int(input("Guess column: "))
            if guess_col not in range(1, len(size) + 1):
                print("Not a valid column, enter a number between 1 - {}".format(len(size)))
            else:
                valid_col = True
        except ValueError:
            print("Not a number, try again")
    return guess_col - 1

# def comp_shot
# def player_shot
# def new_game
# def game_play
# def main()
# size = set_board_size()
# print_board = user_ships(size)

# main()
