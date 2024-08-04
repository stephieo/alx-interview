#!/usr/bin/python3
"""The N queens puzzle
"""
import sys


def is_valid_position(pos, occupied_pos):
    """Check if a position is valid for placing a queen"""
    for i in range(len(occupied_pos)):
        if (
            occupied_pos[i] == pos or
            occupied_pos[i] - i == pos - len(occupied_pos) or
            occupied_pos[i] + i == pos + len(occupied_pos)
        ):
            return False
    return True


def place_queens(n, index, occupied_pos, solutions):
    """Place queens on the board and collect valid positsions"""
    if index == n:
        solutions.append(occupied_pos[:])
        return

    for i in range(n):
        if is_valid_position(i, occupied_pos):
            occupied_pos.append(i)
            place_queens(n, index + 1, occupied_pos, solutions)
            occupied_pos.pop()


def solve_nqueens(n):
    solutions = []
    place_queens(n, 0, [], solutions)
    return solutions


def init():
    """Initialize and validate input"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def n_queens():
    """Main function to solve and print the N queens solutions"""
    n = init()
    solutions = solve_nqueens(n)
    for solution in solutions:
        print([[i, solution[i]] for i in range(len(solution))])


if __name__ == '__main__':
    n_queens()
