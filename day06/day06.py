#!/usr/bin/env python3
"""Day 6: Probably a Fire Hazard

Because your neighbors keep defeating you in the holiday house decorating
contest year after year, you've decided to deploy one million lights
in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed
you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction;
the lights at each corner are at 0,0, 0,999, 999,999, and 999,0.
The instructions include whether to turn on, turn off, or toggle various
inclusive ranges given as coordinate pairs. Each coordinate pair represents
opposite corners of a rectangle, inclusive; a coordinate pair like
0,0 through 2,2 therefore refers to 9 lights in a 3x3 square.
The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights
by doing the instructions Santa sent you in order.

"""
import re

DATA_PATTERN = (
    r'(.+) '  # command: 'turn on', 'turn off', or 'toggle'
    r'(\d+),(\d+)'  # starting coordinates
    r' through '
    r'(\d+),(\d+)'  # ending coordinates
)

# used for part 1
# the commands actually mean what they say.
on_off_commands = {
    'turn on': lambda value: 1,
    'turn off': lambda value: 0,
    'toggle': lambda value: 0 if value else 1,
}

# used for part 2
# `turn on` actually means increase the brightness by 1.
# `turn off` actually means decrease the brightness by 1, to a minimum of zero.
# `toggle` actually means increase the brightness by 2.
brightness_commands = {
    'turn on': lambda value: value + 1,
    'turn off': lambda value: value - 1 if value else 0,
    'toggle': lambda value: value + 2,
}


def modify_grid(grid, line, commands):
    """Modify the grid according to the instructions in `line`.

    Args:
      grid (list of lists of int): The light grid.
      line (str): A single instruction of the format
        '<command> <x1>,<y1> through <x2>,<y2>'.
        command can be either 'turn on', 'turn off', or 'toggle',
        (x1, y1) and (x2, y2) are rectangle point coordinates.
      commands (dict): Mapping of commands to modification functions.

    """
    command, x1, y1, x2, y2 = re.match(DATA_PATTERN, line).groups()
    modify = commands[command]

    for x in range(int(x1), int(x2) + 1):
        for y in range(int(y1), int(y2) + 1):
            grid[y][x] = modify(grid[y][x])


def total_brightness(grid):
    """Calculate the total brightness of the light grid.

    Total brightness is the sum of all the cells in the list of lists.

    Args:
      grid (list of lists of int): The light grid.

    Returns:
      int: Total brightness

    """
    return sum(sum(row) for row in grid)


def main():
    import sys

    on_off_grid = [[False] * 1000 for _ in range(1000)]
    brightness_grid = [[0] * 1000 for _ in range(1000)]

    with open(sys.argv[1]) as f:
        for line in f:
            modify_grid(on_off_grid, line, on_off_commands)
            modify_grid(brightness_grid, line, brightness_commands)

    print(total_brightness(on_off_grid))
    print(total_brightness(brightness_grid))


if __name__ == '__main__':
    main()
