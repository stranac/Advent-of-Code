#!/usr/bin/env python3
"""Day 13: Knights of the Dinner Table

In years past, the holiday feast with your family hasn't gone so well.
Not everyone gets along! This year, you resolve, will be different.
You're going to find the optimal seating arrangement and avoid all those
awkward conversations.

You start by writing up a list of everyone invited and the amount their
happiness would increase or decrease if they were to find themselves sitting
next to each other person. You have a circular table that will be just big
enough to fit everyone comfortably, and so each person will have exactly
two neighbors.

What is the total change in happiness for the optimal seating arrangement
of the actual guest list?

Part 2:
In all the commotion, you realize that you forgot to seat yourself. At this
point, you're pretty apathetic toward the whole thing, and your happiness
wouldn't really go up or down regardless of who you sit next to. You assume
everyone else would be just as ambivalent about sitting next to you, too.

What is the total change in happiness for the optimal seating arrangement
that actually includes yourself?

"""
import itertools
from collections import defaultdict


def parse_file(filename):
    """Parse the contents of the file into a happiness dict.

    Args:
      filename (str): Path to the input file.
        Lines are in the format:
          "<P1> would <gain/lose> <n> happiness units by sitting next to <P2>."

    Returns:
      dict of dict: Mapping  of each persons happiness if seated next to
        each of the others.

    """
    happiness = defaultdict(dict)

    with open(filename) as f:
        for line in f:
            parts = line.split()

            first = parts[0]
            second = parts[-1].strip('.')
            sign = +1 if parts[2] == 'gain' else -1
            n = int(parts[3])

            happiness[first][second] = sign * n

    return happiness


def happiness_totals(happiness):
    """Find happiness totals for each sitting arrangement.

    Args:
      happiness (dict of dict): Mapping  of each persons happiness
        if seated next to each of the others.

    Yields:
      int: Happiness totals for different sitting arrangements.

    """
    first, *rest = happiness

    for perm in itertools.permutations(rest):
        # make arrangement circular by making the first and last seat same one
        arrangement = (first,) + perm + (first,)
        yield happiness_total(arrangement, happiness)


def happiness_total(arrangement, happiness):
    """Find the happiness total of a given seating arrangement.

    Args:
      arrangement (tuple): Seating arrangement.
      happiness (dict of dict): Mapping  of each persons happiness
        if seated next to each of the others.

    Returns:
      int: Happiness total.

    Examples:
    >>> happiness = {
        'Alice': {'Bob': 54, 'Carol': -79, 'David': -2},
        'Bob': {'Alice': 83, 'Carol': -7, 'David': -63},
        'Carol': {'Alice': -62, 'Bob': 60, 'David': 55},
        'David': {'Alice': 46, 'Bob': -7, 'Carol': 41},
    }
    >>> happiness_total(('Alice', 'Bob', 'Carol', 'David', 'Alice'), happiness)
    330
    >>> happiness_total(('Bob', 'David', 'Carol', 'Alice', 'Bob'), happiness)
    22

    """
    return sum(
        happiness[person1][person2] + happiness[person2][person1]
        for person1, person2 in zip(arrangement, arrangement[1:])
    )


def main():
    import sys

    happiness = parse_file(sys.argv[1])
    print(max(happiness_totals(happiness)))

    for person in happiness.copy():
        happiness[person]['me'] = happiness['me'][person] = 0
    print(max(happiness_totals(happiness)))


if __name__ == '__main__':
    main()
