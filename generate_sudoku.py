# Generate board.

from solve_sudoku import solve, print_board
from random import randint

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def fill_board(board):
    """
    Fill a blank board.\n
    Arguments:\n
        board: A blank board.
    """
    # X Axis.
    for i in range(0, len(board)):
        temp = list()
        # Y Axis
        for j in range(0, len(board[i])):
            if i == 0:          # Selecting First row.
                while board[i][j] == 0:
                    number = randint(1, 9)
                    if number not in temp:
                        temp.append(number)
                        board[i][j] = number

            else:
                solve(board)
    print_board(board)


if __name__ == "__main__":
    fill_board(board)
