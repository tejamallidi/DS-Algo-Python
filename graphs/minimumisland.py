'''
Write a function, minimumIsland, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the size of the smallest island. An island is a vertically or horizontally connected region of land.

You may assume that the grid contains at least one island.
'''


def minimum_island(grid):
    visited = set()
    min = len(grid) * 2  # consider a bigger value
    # iterate through all the rows, columns of the grid
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = explore(grid, r, c, visited)
            if size > 0 and size < min:  # check if size != 0 to avoid the corner case where there is no island as per assumption is minimum of 1 island
                min = size
    return min


def explore(grid, r, c, visited):
    # check for bounds to verify the position
    row_inbounds = 0 <= r and r < len(grid)
    col_inbounds = 0 <= c and c < len(grid[0])
    if (not row_inbounds or not col_inbounds):
        return 0

    # avoid water grids
    if grid[r][c] == 'W':
        return 0

    # check if position was already visited
    pos = f'{r},{c}'
    if pos in visited:
        return 0

    visited.add(pos)

    size = 1  # include the current valid node
    # calculate the count in each valid, possible iteration
    size += explore(grid, r-1, c, visited)
    size += explore(grid, r, c-1, visited)
    size += explore(grid, r+1, c, visited)
    size += explore(grid, r, c+1, visited)

    return size


if __name__ == '__main__':
    grid = [
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W'],
    ]
    print(minimum_island(grid))
