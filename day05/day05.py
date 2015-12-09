#!/usr/bin/env python3
"""Day 5: Doesn't He Have Intern-Elves For This?

Santa needs help figuring out which strings
in his text file are naughty or nice.

How many strings are nice?
There are two criteria for determining if a string is nice.
"""
import re

VOWEL_PATTERN = r'[aeiou]'
BAD_SUBSTRING_PATTERN = r'ab|cd|pq|xy'
DOUBLE_LETTER_PATTERN = r'(.)\1'

REPEATING_PAIR_PATTERN = r'(..).*\1'
DOUBLE_LETTER_WITH_SEPARATOR_PATTERN = r'(.).\1'


def is_nice_part_one(s):
    """Determine if a string is nice.

    The string is nice if:
      - it contains at least 3 vowels (aeiou)
      - it contains at least one letter that appears twice in a row
      - it does not contain the strings `ab`, `cd`, `pq`, or `xy`

    Args:
      s (string)

    Returns:
      bool: `True` if the string is nice, `False` if it is naughty.

    """
    return (
        len(re.findall(VOWEL_PATTERN, s)) > 2 and
        re.search(DOUBLE_LETTER_PATTERN, s) and
        not re.search(BAD_SUBSTRING_PATTERN, s)
    )


def is_nice_part_two(s):
    """Determine if a string is nice.

    The string is nice if:
      - contains a pair of letters that appears at least twice in the string
      - contains two of the same letter appearing with
          exactly one letter between them

    Args:
      s (string)

    Returns:
      bool: `True` if the string is nice, `False` if it is naughty.

    """
    return (
        re.search(REPEATING_PAIR_PATTERN, s) and
        re.search(DOUBLE_LETTER_WITH_SEPARATOR_PATTERN, s)
    )


def n_nice(strings, is_nice):
    """Determine the number of nice strings.

    Args:
      strings (list of strings)
      is_nice (function): Criterium used to decide if a string is nice.

    Returns:
      int: Number of nice strings.

    """
    return sum(1 for s in strings if is_nice(s))


def main():
    with open('input') as f:
        strings = f.read().splitlines()

    print(n_nice(strings, is_nice_part_one))
    print(n_nice(strings, is_nice_part_two))


if __name__ == '__main__':
    main()
