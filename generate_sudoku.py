# Generate board.

import solve_sudoku
from random import randint


def generate_board():
    """
    Fill a blank board.\n
    Arguments:\n
        board: A blank board.
    """
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
                solve_sudoku.solve(board)

    return board
