from sudoku.tools import *

def solver(board, verbose=True):
    """ solve a sudoku board
    """
    board_copy = board.copy()
    empty = find_empty(board_copy)

    if len(empty):
        iter_ = 0
        count = 0
        while True:
            count += 1
            print(count, end='\r')
            next_ava = check_next_ava(board_copy, empty[iter_])
            if next_ava != 0:
                board_copy[empty[iter_][0], empty[iter_][1]] = next_ava
                iter_ += 1
            else:
                board_copy[empty[iter_][0], empty[iter_][1]] = next_ava
                iter_ -= 1

            if iter_ >= len(empty):
                if verbose:
                    print('Solved')
                break

    else:
        if verbose:
            print('No empty cell to solve, return original board')

    return board_copy
