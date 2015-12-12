#!/usr/bin/env python3
"""Advent of Code - Day 1

Santa is trying to deliver presents in a large apartment building, but he
can't find the right floor - the directions he got are a little confusing.
He starts on the ground floor (floor 0) and then follows the instructions
one character at a time.

An opening parenthesis, (, means he should go up one floor,
and a closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep;
he will never find the top or bottom floors.

"""


def final_floor(instructions):
    """Calculate the floor Santa will end up on.

    Args:
      instructions (string): Santa's movement instructions.
        '(' means go up, ')' means go down.

    Returns:
      int: Final floor

    Examples:
      >>> final_floor('(())')
      0
      >>> final_floor('(()(()(')
      3
      >>> final_floor(')())())')
      -3

    """
    return sum(1 if c == '(' else -1 for c in instructions)


def enters_basement(instructions):
    """Find the first instruction that makes Santa enter the basement.

    Args:
      instructions (string): Santa's movement instructions.
        '(' means go up, ')' means go down.

    Returns:
      int: Position of the first instruction at which Santa enter the basement

    Examples:
      >>> enters_basement(')')
      1
      >>> enters_basement('()())')
      5

    """
    floor = 0
    for i, instruction in enumerate(instructions, 1):
        if instruction == '(':
            floor += 1
        else:
            floor -= 1
        if floor < 0:
            return i


def main():
    import sys

    with open(sys.argv[1]) as f:
        instructions = f.read()

    print(final_floor(instructions))
    print(enters_basement(instructions))


if __name__ == '__main__':
    main()
