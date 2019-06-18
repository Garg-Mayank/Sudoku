# Board Output.


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
