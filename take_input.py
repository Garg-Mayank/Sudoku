"""
Take input of the board and minor other function to clear the screen.
"""


import solve_sudoku

input_help = 'If sudoku has BLANK SPACE, then enter 0'


def clrscr():
    """
    Clears the terminal screen.
    """
    import os
    name = os.name
    if name == "nt":
        os.system('cls')
    elif name == "posix":
        os.system('clear')


def input_board():
    """
    Enter the element of board.
    """
    board = list()

    for i in range(0, 9):
        print(input_help)
        print('\n')
        print('Enter numbers for row ' + str(i + 1))
        j = input('Enter 9 numbers' + '\n').split()
        board.append(j)

    clrscr()

    return board
