# Sudoku Solver.

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(board):
    """
    The backtraking algorithm.\n
    Arguments:\n
        board: The board to be solved.
    """
    find = find_empty(board)
    if not find:
        return True     # We found a solution.
    else:
        row, column = find

    for i in range(1, 10):
        if check_validity(board, i, (row, column)):
            board[row][column] = i

            if solve(board):
                return True
            # Here we resets the last value back to zero
            board[row][column] = 0

    return False


def check_validity(board, number, pos):
    """
    Checks the validity of the board.\n
    Arguments:\n
        board: The sudoku board.
        number: Number to insert.
        pos: The position of the number. It is (X, Y) tuple.
    """
    # Check Row.
    for i in range(0, len(board[0])):
        if board[pos[0]][i] == number and pos[1] != i:
            return False

    # Check Column.
    for i in range(0, len(board[0])):
        if board[i][pos[1]] == number and pos[0] != i:
            return False

    # Check Small Box.
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i, j) != pos:
                return False

    return True


def print_board(board):
    """
    Print the sudoku board in a specific pattern.\n
    Arguments:\n
        board: The board to be printed.
    """
    for i in range(0, len(board)):
        if i % 3 == 0 and i != 0:
            print('--------------------------')

        for j in range(0, len(board[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end=" ")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    """
    Finding the empty space in Sudoku.\n
    Here empty space is denoted by "0".\n
    Arguments:\n
        board: The sudoku board
    """
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None


if __name__ == "__main__":
    print_board(board)
    solve(board)
    print('___________________________________________')
    print()
    print_board(board)
