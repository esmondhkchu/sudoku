from sudoku.tools import *
from sudoku.solver import *

def generate_board():
    """ generate a soduku board
    """
    while True:
        row_1 = np.random.choice(np.arange(1,10), 9, False)
        row_2 = np.random.choice(np.arange(1,10), 9, False)

        if 0 not in row_1 - row_2:
            break

    while True:

        row_num_1, row_num_2 = np.random.choice(np.arange(0,9), 2, False)

        if np.abs(row_num_1 - row_num_2) >= 3:
            break

    template = np.zeros((9,9)).astype(int)
    template[row_num_1,:] = row_1
    template[row_num_2,:] = row_2

    solved = solver(template, False)
    return solved

def drop_values(board, remove_num):
    """ drop values from a solved board

    Parameters: board (np.array) - a solved board
                remove_num (int) - total numbers of cell to remove

    Returns: solved (np.array) - a solved board with n cells values removed
    """
    if remove_num > 64:
        raise ValueError('Must contains more than 17 non-empty cells')

    solved = board.copy()
    counter = 0
    while True:
        i,j = np.random.randint(0,9,2)
        if solved[i,j] != 0:
            solved[i,j] = 0
            counter += 1
        else:
            continue

        if counter == remove_num:
            break

    return solved
