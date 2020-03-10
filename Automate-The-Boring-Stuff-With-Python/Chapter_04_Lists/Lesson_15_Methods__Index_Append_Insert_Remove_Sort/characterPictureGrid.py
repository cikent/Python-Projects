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

# Define grid: A List that contains Lists
heartGrid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Debug initial print of grid
print(str(heartGrid))

# Define String variables to hold the grid
# gridRow = len(heartGrid)                   # gridRow == grid's len which is the Index # in the Parent List
# gridColumn = len(heartGrid[gridRow])       # gridColumn == grid's 

# Define a function to print the Grid
def printGrid(gridList):
    # Iterate through List(s)
    for x in range(len(gridList)):
            for y in range(len(gridList[y])):
                print(gridList[x][y], end='')

printGrid(heartGrid)