#!/usr/bin/python3
def island_perimeter(grid):
    """
    Returns the perimeter of the island described in the grid.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:  # Land cell
                # Check all four directions
                if row == 0 or grid[row - 1][col] == 0:  # Top
                    perimeter += 1
                if row == rows - 1 or grid[row + 1][col] == 0:  # Bottom
                    perimeter += 1
                if col == 0 or grid[row][col - 1] == 0:  # Left
                    perimeter += 1
                if col == cols - 1 or grid[row][col + 1] == 0:  # Right
                    perimeter += 1

    return perimeter

