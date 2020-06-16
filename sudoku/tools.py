import numpy as np

def find_empty(board):
    """ find all the empty position

    Parameters: board (np.array) -  the original 9x9 sudoku board

    Returns: (list) - a list contains tuples of empty positions
    """
    row_idx, col_idx = np.where(board == 0)
    return [(i,j) for i,j in zip(row_idx, col_idx)]

def check_valid(board, pos, sub):
    """ check a number in a specific position is valid or nor

    Parameters: board (np.array) - the original board
                pos (tuple/list) - the position to be checked
                sub (int) - the substitute number to be checked

    Returns: (boo) - True denotes valid, o/w False
    """
    # check row and col
    row = sub in board[pos[0],:]
    col = sub in board[:,pos[1]]

    # check 3x3 box
    row_sec = pos[0] // 3
    col_sec = pos[1] // 3
    sec = board[row_sec*3:(row_sec+1)*3, col_sec*3:(col_sec+1)*3].flatten()
    box = sub in sec

    if np.sum([row, col, box]) == 0:
        return True
    else:
        return False

def check_next_ava(board, pos):
    """ check next available in an ascending order, i.e. from 0-9

    Parameters: board (np.array) - the original board
                pos (tuple/list) - the position to be checked

    Results: (int/boo) - 1-9, the next available or if not possible to find any, then return False
    """
    return_val = 0
    for i in range(board[pos[0],pos[1]], 10):
        if check_valid(board, pos, i):
            return_val = i
            break
        else:
            continue

    return return_val
