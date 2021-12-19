'''
Write a function, islandCount, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the number of islands on the grid. An island is a vertically or horizontally connected region of land.
'''


def island_count(grid):
    visited = set()
    count = 0
    # iterate through all the rows, columns of the grid
    for r in range(len(grid)):
        for c in range(len(grid[0])):  # iterating through column
            if explore(grid, r, c, visited):
                count += 1
    return count


def explore(grid, r, c, visited):
    # check if the r,c is a valid position in the grid
    row_inbounds = 0 <= r and r < len(grid)
    col_inbounds = 0 <= c and c < len(grid[0])
    if (not row_inbounds or not col_inbounds):
        return False

    # if the grid at current pos is 'W' return false
    if grid[r][c] == 'W':
        return False

    # check if the position was already visited
    pos = f'{r},{c}'
    if pos in visited:
        return False

    visited.add(pos)

    # after handling all base conditions continue with the execution
    explore(grid, r-1, c, visited)
    explore(grid, r, c-1, visited)
    explore(grid, r+1, c, visited)
    explore(grid, r, c+1, visited)

    return True


if __name__ == '__main__':
    grid = [
        ['L', 'W', 'W', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['W', 'L', 'W', 'L', 'W'],
        ['W', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'L', 'L', 'L'],
    ]
    print(island_count(grid))
