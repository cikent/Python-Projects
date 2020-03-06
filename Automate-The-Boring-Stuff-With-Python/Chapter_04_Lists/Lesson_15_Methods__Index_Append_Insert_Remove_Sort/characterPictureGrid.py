"""
Requirements: 
1. Print Grid such that it outputs like:
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....
2. asdf

Source: https://automatetheboringstuff.com/chapter4/ -> search for Character Picture Grid
"""

# Define a List
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Debug initial print of grid
print(str(grid))

# Define String variables to hold the grid
gridRow = len(grid)
gridColumn = len(grid[0])

# Define a function to print the Grid
def printGrid(gridList):
        # Iterate through List(s)
        for x in grid[x][y]:
