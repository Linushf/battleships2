from random import randint


def set_board():
    """
    User chooses size of the gaming baord
    """
    size = []
    valid = False
    while valid is not True:
        try:
            board_size = int(input("How big Sea would you like the sea? (2 - 10): "))
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

set_board()