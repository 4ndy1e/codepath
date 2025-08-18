"""
Problem 1: Seeking Safety
The city has been overrun by zombies, and you need to be very careful about how you move about the city. You have a map of the city grid represented by an m x n matrix of 1s (safe zones) and 0s (infected zones). Given a tuple position in the form (row, column) representing your current position in the city grid, implement a function next_moves() that returns a list of tuples representing safe next moves. You may return the moves in any order.

From your current position, you may move to any (row, column) index that is horizontally or vertically adjacent such that row and column are both valid indices in grid. A move is safe if it has value 1.

Input: tuple (starting position (row, col)),matrix (m x n, where 1s are safe and 0s are infected)
Output: list of tuples (represents the tuples of next moves we can make)
Constraints:
    - next moves are up, left, right, and down
Edge Cases:
    - 
    
Plan: Use the given position and get the up, left, right, down positions of the starting position. A next move is possible if the 
value is 1 and it is within the matrix. 

seperate the position into the row and col

get the total length of the rows
get the total length of the rows

define possible directions 
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] (left, right, up, down)

create a results variable to store the possible next moves

for row_direction, col_direction in directions
    curr_row = position row + row_direction
    curr_col = position col + col_direction
    
    if (curr_row, curr_col) is in the matrix and it has a value of 1, add it to the results

return the results
"""

def next_moves(position, grid):
    positionRow, positionCol = position
    
    totalRows = len(grid)
    totalCols = len(grid[0])
    
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    results = []
    
    for rowDirection, colDirection in directions:
        # calculate new position
        currRow = positionRow + rowDirection
        currCol = positionCol + colDirection
        
        if (0 <= currRow < totalRows and 0 <= currCol < totalCols) and grid[currRow][currCol] == 1:
            results.append((currRow, currCol))
    
    return results

grid = [
    [0, 0, 0, 1, 1], # Row 0
    [0, 0, 0, 1, 1], # Row 1
    [1, 1, 1, 0, 0], # Row 2
    [1, 1, 1, 1, 0], # Row 3
    [0, 0, 0, 1, 0]  # Row 4
]

position_1 = (3, 2)
position_2 = (0, 4)
position_3 = (0, 1)

print(next_moves(position_1, grid))
print(next_moves(position_2, grid))
print(next_moves(position_3, grid))