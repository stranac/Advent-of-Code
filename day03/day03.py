#!/usr/bin/env python3
"""Day 3: Perfectly Spherical Houses in a Vacuum

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location,
and then an elf at the North Pole calls him via radio and tells him where
to move next. After each move, he delivers another present to the house
at his new location.

How many houses receive at least one present?


The next year, to speed up the process, Santa creates a robot version
of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to
the same starting house), then take turns moving based on instructions from
the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

"""


def visited_houses(instructions):
    """Determine which houses were visited by Santa (or Robo-Santa).

    Args:
      instructions (string): Santa's movement instructions.
        Moves one house to the north `^`, south `v`, east `>`, or west `<`.

    Returns:
      set of tuples: Coordinates of the visited houses.

    Examples:
      >>> visited_houses('>')
      {(1, 0), (0, 0)}
      >>> visited_houses('^>v<')
      {(0, 1), (1, 0), (0, 0), (1, 1)}
      >>> visited_houses('^v^v^v^v^v')
      {(0, 1), (0, 0)}

    """
    x = y = 0
    visited = {(x, y)}
    for c in instructions:
        if c == '^':
            y += 1
        elif c == 'v':
            y -= 1
        elif c == '>':
            x += 1
        elif c == '<':
            x -= 1
        visited.add((x, y))
    return visited


def n_visited(*args):
    """Calculate the number of houses visited.

    Each Santa visits his own set of houses.
    The result is the total number of visited houses.

    Args:
      *args (strings): Instruction sets for each Santa.

    Returns:
      int: Total number of visited houses.

    """
    visited = set()
    for instructions in args:
        visited |= visited_houses(instructions)
    return len(visited)


def main():
    import sys

    with open(sys.argv[1]) as f:
        instructions = f.read()

    # all the moves are Santa's
    print(n_visited(instructions))
    # half the moves are Santa's, half are the robot's
    santa_moves = instructions[::2]
    robot_moves = instructions[1::2]
    print(n_visited(santa_moves, robot_moves))


if __name__ == '__main__':
    main()
