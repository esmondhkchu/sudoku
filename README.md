# A Sudoku solver

## Demo
```python
>>> from sudoku import *

>>> board = generate_board()
>>> print('Generated Board: \n')
>>> for i in board:
        print(i)

Generated Board:

[1 3 2 4 5 7 6 8 9]
[4 5 6 1 9 8 2 3 7]
[7 8 9 6 2 3 1 4 5]
[5 2 4 3 8 6 9 7 1]
[3 1 7 9 4 2 5 6 8]
[6 9 8 5 7 1 4 2 3]
[2 4 1 7 3 9 8 5 6]
[9 7 5 8 6 4 3 1 2]
[8 6 3 2 1 5 7 9 4]

>>> unsolved = drop_values(board, 60)
>>> print('Unsolved Board (empty box: 60): \n')
>>> for i in unsolved:
        print(i)

Unsolved Board (empty box: 60):

[0 0 2 4 5 0 6 0 0]
[0 0 0 0 9 0 0 0 0]
[0 0 0 0 0 3 0 4 0]
[0 0 4 3 0 0 0 0 0]
[0 0 0 0 0 0 5 0 0]
[0 0 8 5 0 0 0 0 3]
[0 0 0 0 0 9 0 0 0]
[0 0 0 0 0 0 3 0 2]
[0 6 3 0 0 5 0 9 4]

>>> solved = solver(unsolved)
>>> print('Solved Board: \n')
>>> for i in solved:
        print(i)

Solved
Solved Board:

[1 3 2 4 5 7 6 8 9]
[4 5 6 1 9 8 2 3 7]
[7 8 9 6 2 3 1 4 5]
[5 1 4 3 6 2 9 7 8]
[3 2 7 9 8 4 5 1 6]
[6 9 8 5 7 1 4 2 3]
[2 4 5 7 3 9 8 6 1]
[9 7 1 8 4 6 3 5 2]
[8 6 3 2 1 5 7 9 4]
```
