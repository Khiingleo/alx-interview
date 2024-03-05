#!/usr/bin/python3
"""
defines a function island perimeter
"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    """
    perimeter = 0

    def is_water(i, j):
        """
        check if a cell is land or water
        """
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0])\
                or grid[i][j] == 0:
            return True
        return False

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                if is_water(i - 1, j):
                    perimeter += 1
                if is_water(i + 1, j):
                    perimeter += 1
                if is_water(i, j - 1):
                    perimeter += 1
                if is_water(i, j + 1):
                    perimeter += 1

    return perimeter
