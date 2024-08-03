#!/usr/bin/python3
""" Pascal's Triangle 
"""

def pascal_triangle(n):
"""
    Create a Pascal's Triangle .

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists.
        Each inner list is a row in theTriangle.
        Empty list if n <= 0 or not an integer.
    """
    if not isinstance(n, int) or n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
