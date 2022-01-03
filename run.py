from random import randint


def set_board_size():
    """
    The user chooses size of the gaming board.
    """
    size = []
    valid = False
    while valid is not True:
        try:
            board_size = int(input("How big would you like the sea? (2 - 10): "))
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

#def random_row
#def random_col
#def find_ship
#def print_board(size)
#def row_guess(size)
#def col_guess(size)
#def comp_shot
#def player_shot
#def new_game
#def game_play
#def main()