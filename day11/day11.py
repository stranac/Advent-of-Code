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


def substrings(s, lenght=1):
    """Generate all `lenght` long substrings of `s`.

    Args:
      s (str)
      lenght (int)

    Yields:
      str: Substrings of s.

    """
    for i in range(len(s) - lenght):
        yield s[i:i + lenght]


def valid(password):
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
    if not re.search(TWO_PAIR_RE, password):
        return False
    return any(s in ascii_lowercase for s in substrings(password, 3))


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
    s = min_candidate(s, next_letters)

    if s[-1] == 'z':
        return next_string(s[:-1], next_letters) + 'a'
    else:
        return s[:-1] + next_letters[s[-1]]


def min_candidate(s, next_letters):
    """Find first string starting from `s` that contains no invalid letters.

    We get this string by increasing the first invalid string and
    replacing all the following letters by 'a's.

    Args:
      s (str): Starting string.
      next_letters (dict): Mapping of each letter to the next one.

    Returns:
      str: First potentially valid string.

    """
    i = first_index(s, search_for='ilo')
    if i > 0:
        remaining = len(s) - i
        s = s[:i] + next_letters[s[i]] + 'a' * remaining
    return s


def first_index(s, search_for):
    """Find the first index of any element of `search_for` in `s`.

    Args:
      s (str): String in which we search.
      search_for (collection): Elements we are looking for.

    Returns:
      int: First index, or -1 if not found.

    """
    for i, c in enumerate(s):
        if c in search_for:
            return i
    return -1


def next_valid_password(password, next_letters):
    """Generate the next valid password. For rules, check `:func:valid`.

    Args:
      password (str): Current password.
      next_letters (dict): Mapping of each letter to the next one.

    Returns:
      str: Next valid password.

    """
    while True:
        password = next_string(password, next_letters)
        if valid(password):
            return password


def main():
    password = 'hxbxwxba'
    next_letters = create_next_letters()

    for _ in range(2):
        password = next_valid_password(password, next_letters)
        print(password)


if __name__ == '__main__':
    main()
