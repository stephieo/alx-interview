#!/usr/bin/python3
"""
module for island_perimeter interview
find perimeter of island in body of water
"""

def island_perimeter(grid):
    """
    Calculate and return the perimeter of the island described in grid.
    Args:
        grid (list): 2D list of integers representing the grid
    
    Returns:
        int: Perimeter of the island
    """
    if not grid:
        return 0
    
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Each land cell contributes 4 to the perimeter initially
                perimeter += 4
                
                # Check the cell above
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                
                # Check the cell to the left
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    
    return perimeter   
