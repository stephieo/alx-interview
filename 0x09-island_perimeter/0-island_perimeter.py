#!/usr/bin/python3
"""
island_perimeter interview
find perimeter of island in body of water
""""

def island_perimeter(grid):
    """
    Calculate and return the perimeter of the island described in grid.
    """
    if not grid:
        return 0
    
 perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
   
