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
# print(str(heartGrid))

# Define String variables to hold the grid
gridRow = len(heartGrid)                   # gridRow == heartGrid's # of Indecies in the Parent List Reference
gridColumn = len(heartGrid[0])             # gridColumn == heartGrid's # of Indecies in the Child List Reference

# Define a function to print the Grid v1
def printGridv1(gridList):
    # Iterate through Row List(s) 1st
    for x in range(gridRow):
            print()
            for y in range(gridColumn):
                print(gridList[x][y], end='')

# Define a function to print the Grid v2
def printGridv2(gridList):
    # Iterate through Column List(s) 1st
    for y in range(gridColumn):
            for x in range(gridRow):
                print(gridList[x][y], end='')
            print()

# printGridv1(heartGrid)
printGridv2(heartGrid)
