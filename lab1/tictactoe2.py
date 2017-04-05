#!/usr/bin/env python3
"""
File: tictactoe2.py

Problem: Print an Ultimate Tic-Tac-Toe board
"""

three_square = "|".join(["  ", "  ", "  "])
row_square = "H".join([three_square, three_square, three_square])
row_divider = row_square.replace(" ","-").replace("|","+")
grid_divider = row_square.replace(" ","=").replace("|","=").replace("H","+")
three_grid = "\n".join([row_square, row_divider, row_square, row_divider, row_square])
nine_grid = "\n{}\n".format(grid_divider).join([three_grid, three_grid, three_grid])

print(nine_grid)

