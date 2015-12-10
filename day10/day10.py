#!/usr/bin/env python3
"""Day 10: Elves Look, Elves Say

Today, the Elves are playing a game called look-and-say. They take turns
making sequences by reading aloud the previous sequence and using that
reading as the next sequence. For example, `211` is read as
"one two, two ones", which becomes `1221`.

"""
from itertools import groupby


def look_and_say(s):
    """Generate the next element of the look-and-say sequence.

    Look-and-say sequences are generated iteratively, using the previous value
    as input for the next step. For each step, take the previous value,
    and replaceeach run of digits (like `111`) with the number of digits (`3`)
    followed by the digit itself (`1`).

    Args:
      s (str): Previous element of the look-and-say.

    Returns:
      str: Next element of the look-and-say.

    Examples:
    >>> look_and_say('1')
    '11
    >>> look_and_say('11')
    '21
    >>> look_and_say('21')
    '1211'
    >>> look_and_say('1211')
    '111221'
    >>> look_and_say('111221')
    312211

    """
    parts = []
    for digit, group in groupby(s):
        length = len(list(group))
        parts.append('{}{}'.format(length, digit))
    return ''.join(parts)


def main():
    sequence = '1113122113'

    for _ in range(40):
        sequence = look_and_say(sequence)

    print(len(sequence))

    for _ in range(10):
        sequence = look_and_say(sequence)

    print(len(sequence))


if __name__ == '__main__':
    main()
