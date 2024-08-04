#!/usr/bin/python3
"""The N queens puzzle 
"""

import sys

def solve_nqueens(row, column):
    solution = [[]]
    for queen in range(row):
        solution = place_queen(queen, column, solution)
    return solution

def place_queen(queen, column, prev_solution):
    safe_position = []
    for array in prev_solution:
        for x in range(column):
            if is_safe(queen, x, array):
                safe_position.append(array + [x])
    return safe_position

def is_safe(q, x, array):
    if x in array:
        return False
    else:
        return all(abs(array[column] - x) != q - column for column in range(q))

def init():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigi
