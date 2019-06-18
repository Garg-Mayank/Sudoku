# Main File.

import generate_sudoku
import solve_sudoku
import take_input
import board_output


def main():
    """
    The main file to execute the program.
    """
    print('1. Generate a new sudoku! ')
    print('2. Solve a Sudoku! ')
    choice = int(input('Enter your choice: '))

    if choice == 1:
        board = generate_sudoku.generate_board()
        board_output.print_board(board)

    if choice == 2:
        board = take_input.input_board()
        print('The board you entered is: ')
        board_output.print_board(board)

        print('Solving Board')
        solve_sudoku.solve(board)
        board_output.print_board(board)


if __name__ == "__main__":
    main()
