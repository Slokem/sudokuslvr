import numpy as np
from sudokuslvr.sudoku import Grid




# creating a grid and print the blob for display
testing_list = np.zeros((81,), dtype=int)
print(testing_list)

x = Grid()
x.add_blob(testing_list)
x.print_blob()
