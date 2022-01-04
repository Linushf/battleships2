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


def comp_shot(size, comp_guess_count, comp_row, comp_col):
    """
    Enemy (computer) choose a random, and valid, coordinate to shot.
    """
    valid_comp_shot = False
    while valid_comp_shot is not True:
        attack_row = random_row(size)
        attack_col = random_col(size)
        if size[attack_row][attack_col] == "#":
            print("Enemy sunk your ship and you lose")
            print("Computer sank your ship in {} tries".format(comp_guess_count))
            valid_comp_shot = True
            return True
        elif size[attack_row][attack_col] != "O":
            # Prevents computer duplicate coordinates
            continue
        elif attack_row == comp_row and attack_col == comp_col:
            # Prevents computer from shoting their own ship
            continue
        else:
            size[attack_row][attack_col] = "*"
            print(" - Computers turn - ")
            print_board(size)
            valid_comp_shot = True
    return False


def user_shot(size, user_guess_count, comp_row, comp_col):
    """
    Function to take user input and uses guess_row and guess _col
    """
    valid_user_shot = False
    while valid_user_shot is not True:
        guess_row = row_guess(size)
        guess_col = col_guess(size)

        if size[guess_row][guess_col] == "*":
            print("You've already shot at that location, try again")
        elif size[guess_row][guess_col] == "#":
            print("Do not kill yourself...")
        elif guess_row != comp_row or guess_col != comp_col:
            size[guess_row][guess_col] = "X"
            print(" - Users turn - ")
            print_board(size)
            print(" - You missed - ")
            valid_user_shot = True
        else:
            print("You sunk enemy battleship!")
            print("It took {} tries to win".format(user_guess_count))
            return True
    return False



# def new_game
# def game_play
# def main()
# main()
