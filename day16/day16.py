#!/usr/bin/env python3
"""Your Aunt Sue has given you a wonderful gift, and you'd like to
send her a thank you card. However, there's a small problem:
she signed it "From, Aunt Sue". You have 500 Aunts named "Sue".

So, to avoid sending the card to the wrong person, you need to figure out
which Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you
the gift. You open the present and, as luck would have it, good ol' Aunt Sue
got you a My First Crime Scene Analysis Machine!

The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few
specific compounds in a given sample, as well as how many distinct kinds of
those compounds there are.

Part 2:
Something in the MFCSAM's instructions catches your eye.
Apparently, it has an outdated retroencabulator, and so the output
from the machine isn't exact values - some of them indicate ranges.

In particular, the cats and trees readings indicates that there are greater
than that many (due to the unpredictable nuclear decay of cat dander and
tree pollen), while the pomeranians and goldfish readings indicate that there
are fewer than that many (due to the modial interaction of magnetoreluctance).

"""
import re

INFO_RE = r'(\w+): (\d+)'

MFCSAM_output = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

LOWER = {'pomeranians', 'goldfish'}
HIGHER = {'cats', 'trees'}


def parse_line(line):
    """Extract known information about an aunt.

    Args:
      line (str): A line containing the information.

    Returns:
      dict: Aunt's data.

    """
    data = {}
    for info, n in re.findall(INFO_RE, line):
        data[info] = int(n)
    return data


def find_aunt(data, aunts, lowest=set(), highest=set()):
    """Find an aunt with all matching data.

    Args:
      data (dict): Known data of wanted aunt.
      aunts (dict): Known data of all aunts.
      lowest (set): Keys representing a higher bound for the value.
      highest (set): Keys representing a lower bound for the value.

    Returns:
      int: Matching aunt's index (1-based).

    """
    for i, aunt in enumerate(aunts, 1):
        if data_matches(data, aunt, lowest, highest):
            return i


def data_matches(data, aunt, lowest=set(), highest=set()):
    """Determine if the aunt matches the data.

    Args:
      data (dict): Known data of wanted aunt.
      aunts (dict): Known data of all aunts.
      lowest (set): Keys representing a higher bound for the value.
      highest (set): Keys representing a lower bound for the value.

    Returns:
      bool: `True` if the data matches, `False` otherwise.

    """
    for key in aunt:
        if key in lowest:
            if data[key] <= aunt[key]:
                return False
        elif key in highest:
            if data[key] >= aunt[key]:
                return False
        else:
            if data[key] != aunt[key]:
                return False
    return True


def main():
    import sys

    aunts = []
    with open(sys.argv[1]) as f:
        for line in f:
            aunts.append(parse_line(line))

    print(find_aunt(MFCSAM_output, aunts))
    print(find_aunt(MFCSAM_output, aunts, LOWER, HIGHER))


if __name__ == '__main__':
    main()
