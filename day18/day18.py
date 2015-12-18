#!/usr/bin/env python3
import copy
import functools


def next_step(grid, corners_on=False):
    """Produce the next step of the animation.

    Args:
      grid (list of lists): Current state of the grid.

    Returns:
      The modified grid.

    """
    return [[new_state(grid, i, j, corners_on)
            for j, light in enumerate(row)] for i, row in enumerate(grid)]


def new_state(grid, i, j, corners_on):
    """Find the next state of the light.

    The state a light should have next is based on its current state
    (on or off) plus the number of neighbors that are on:
      - A light which is on stays on when 2 or 3 neighbors are on,
        and turns off otherwise.
      - A light which is off turns on if exactly 3 neighbors are on,
        and stays off otherwise.

    If `corners_on == True`, always returns '#' (on) for corner lights.

    Returns:
      str: '#' if the light should be on, '.' otherwise.

    """
    if corners_on:
        size = len(grid)
        if i in (0, size - 1) and j in (0, size - 1):
            return '#'

    neighbors_on = live_neighbors(grid, i, j)
    if grid[i][j] == '#' and neighbors_on in (2, 3):
        return '#'
    if grid[i][j] == '.' and neighbors_on == 3:
        return '#'
    return '.'


def live_neighbors(grid, i, j):
    """Count the number of neighboring lights turned on.

    Args:
      grid (list of lists): Current state of the grid.
      i (int): Row of the grid.
      j (int): Column of the grid.

    Returns:
      int: Number of turned-on neighbors of `grid[i][j]`.

    """
    size = len(grid)
    return sum(1 for x, y in neighbors(size, i, j) if grid[x][y] == '#')


@functools.lru_cache(maxsize=10000)
def neighbors(size, i, j):
    """Get the indices of the neighboring cells of `grid[i][j]`.

    Args:
      grid (list of lists): Current state of the grid.
      i (int): Row of the grid.
      j (int): Column of the grid.

    Returns:
      list of tuples: Pairs of neighboring cell coordinates.

    """
    neighbor_list = []

    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di == dj == 0:
                continue
            row, column = i + di, j + dj
            if 0 <= row < size and 0 <= column < size:
                neighbor_list.append((row, column))

    return neighbor_list


def lights_on(grid):
    """Calculate the number of the light that are switched on.

    Args:
      grid (list of lists of int): The light grid.

    Returns:
      int: Number of turned-on lights.

    """
    return sum(sum(1 for light in row if light == '#') for row in grid)


def main():
    import sys

    with open(sys.argv[1]) as f:
        grid1 = [list(line.strip()) for line in f]

    # grid2 is the same, but with corner lights turned on
    grid2 = copy.deepcopy(grid1)
    last = len(grid2) - 1
    grid2[0][0] = grid2[0][last] = grid2[last][0] = grid2[last][last] = '#'

    for _ in range(100):
        grid1 = next_step(grid1, corners_on=False)
        grid2 = next_step(grid2, corners_on=True)

    print(lights_on(grid1))
    print(lights_on(grid2))


if __name__ == '__main__':
    main()
