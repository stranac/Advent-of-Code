#!/usr/bin/env python3
"""Day 11: Corporate Policy

Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires, Santa has
devised a method of coming up with a password based on the previous one.
Corporate policy dictates that passwords must be exactly eight lowercase
letters (for security reasons), so he finds his new password by incrementing
his old password string repeatedly until it is valid.

Incrementing is just like counting with numbers: `xx`, `xy`, `xz`, `ya`, `yb`,
and so on. Increase the rightmost letter one step; if it was `z`, it wraps
around to `a`, and repeat with the next letter to the left until one doesn't
wrap around.

Given Santa's current password, what should his next password be?

"""
import re
from string import ascii_lowercase

TWO_PAIR_RE = r'(.)\1.*(.)\2'


def create_next_letters():
    """Create the dict mapping each letter to the next one, while skipping
    invalid letters (`i`, `l`, `o`). Leave out `z`, which is special.

    """
    pairs = zip(ascii_lowercase, ascii_lowercase[1:])
    mapping = {c1: c2 for c1, c2 in pairs}
    # skip invalid letters
    mapping['h'] = 'j'
    mapping['n'] = 'p'
    mapping['k'] = 'm'

    return mapping


def create_streaks():
    """Generate lenght 3 streaks of consecutive letters.

    Yields:
      str: Lenght 3 streaks of consecutive letters.

    """
    triples = zip(ascii_lowercase, ascii_lowercase[1:], ascii_lowercase[2:])
    return [''.join(t) for t in triples]


def valid(password, streaks):
    """Check if a given password is valid.

    Passwords must include one increasing straight of at least three letters,
    like `abc`, `bcd`, `cde`, and so on, up to `xyz`.
    They cannot skip letters; `abd` doesn't count.

    Passwords may not contain the letters `i`, `o`, or `l`, as these letters
    can be mistaken for other characters and are therefore confusing.
    No need to check this, since those will be skipped during generation.

    Passwords must contain at least two different,
    non-overlapping pairs of letters, like `aa`, `bb`, or `zz`.

    Args:
      password (str): The password.
      streaks (list of str): Streaks of consecutive letters.

    Returns:
      bool: True if password is valid, False if it is not.

    Examples:
      >>> valid('hijklmmn')  # fails #2
      False
      >>> valid('abbceffg')  # fails #1
      False
      >>> valid('abbcegjk')  # fails #3
      False
      >>> valid('abcdffaa')
      True
      >>> valid('ghjaabcc')
      True

    """
    return (
        any(streak in password for streak in streaks) and
        re.search(TWO_PAIR_RE, password)
    )


def next_string(s, next_letters):
    """Generate the next string (lexicographically), skipping the invalid
    letters.

    Args:
      s (str): Current string.
      next_letters (dict): Mapping of each letter to the next one.

    Returns:
      str: Next string.

    Examples:

    >>> next_string('aa')
    'ab'
    >>> next_string('abcd')
    'abce'
    >>> next_string('aeiou')  # i and o are invalid, skip them
    'aejpv'
    >>> next_string('xyz')
    'xza'

    """
    # get rid of invalid characters first
    s = s.replace('i', 'j').replace('l', 'm').replace('o', 'p')

    if s[-1] == 'z':
        return next_string(s[:-1], next_letters) + 'a'
    else:
        return s[:-1] + next_letters[s[-1]]


def next_valid_password(password, next_letters, streaks):
    """Generate the next valid password. For rules, check `:func:valid`.

    Args:
      password (str): Current password.
      next_letters (dict): Mapping of each letter to the next one.
      streaks (list of str): Streaks of consecutive letters.

    Returns:
      str: Next valid password.

    """
    while True:
        password = next_string(password, next_letters)
        if valid(password, streaks):
            return password


def main():
    next_letters = create_next_letters()
    streaks = create_streaks()

    password = 'hxbxwxba'

    for _ in range(2):
        password = next_valid_password(password, next_letters, streaks)
        print(password)


if __name__ == '__main__':
    main()
