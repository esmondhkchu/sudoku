# A Sudoku Generator/Solver

## Demo
```python
>>> from sudoku import *

>>> board = generate_board()
>>> print('Generated Board: \n')
>>> for i in board:
        print(i)

Generated Board:

[1 6 4 2 8 9 5 3 7]
[7 8 9 3 6 5 1 2 4]
[5 3 2 4 1 7 6 9 8]
[2 1 3 5 4 8 7 6 9]
[4 5 6 9 7 1 2 8 3]
[8 9 7 6 3 2 4 1 5]
[3 2 1 8 5 4 9 7 6]
[6 7 5 1 9 3 8 4 2]
[9 4 8 7 2 6 3 5 1]

>>> unsolved = drop_values(board, 50)
>>> print('Unsolved Board (empty box: 50): \n')
>>> for i in unsolved:
        print(i)

Unsolved Board (empty box: 50):

[1 0 0 2 8 0 0 0 0]
[0 0 0 3 0 5 0 0 4]
[0 3 0 4 1 7 0 9 0]
[2 1 3 0 4 8 0 0 0]
[0 5 0 0 0 0 0 8 0]
[8 0 7 0 0 2 4 1 0]
[3 0 1 8 0 0 0 7 0]
[0 0 0 1 0 0 0 0 0]
[0 4 8 0 0 6 0 0 0]

>>> solved = solver(unsolved)
>>> print('Solved Board: \n')
>>> for i in solved:
        print(i)

Solved
Solved Board:

[1 6 4 2 8 9 3 5 7]
[7 8 9 3 6 5 1 2 4]
[5 3 2 4 1 7 6 9 8]
[2 1 3 5 4 8 7 6 9]
[4 5 6 9 7 1 2 8 3]
[8 9 7 6 3 2 4 1 5]
[3 2 1 8 5 4 9 7 6]
[6 7 5 1 9 3 8 4 2]
[9 4 8 7 2 6 5 3 1]
```
