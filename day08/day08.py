#!/usr/bin/env python3
r"""Day 8: Matchsticks

Space on the sleigh is limited this year, and so Santa will be bringing his
list as a digital copy. He needs to know how much space it will take up when
stored.

It is important to realize the difference between the number of characters
in the code representation of the string literal and the number of characters
in the in-memory string itself.

Santa's list is a file that contains many double-quoted string literals,
one on each line. The only escape sequences used are
  `\\` (which represents asingle backslash),
  `\"` (which represents a lone double-quote character),
  and `\x` plus two hexadecimal characters
    (which represents a single character with that ASCII code).

"""


def unescaped_len(s):
    """Calculate the lenght of the in-memory version of `s`.

    Args:
      s (string)

    Returns:
      int: The in-memory lenght of the string

    Examples:
      >>> unescaped_len(r'""')  # ''
      0
      >>> unescaped_len(r'"abc"')  # 'abc'
      3
      >>> unescaped_len(r'"aaa\"aaa"')  # 'aaa"aaa'
      7
      >>> unescaped_len(r'"\x27"')  # "'"
      1

    """
    # subtracting two for the enclosing quotes
    return len(s.encode('utf-8').decode('unicode_escape')) - 2


def escaped_len(s):
    """Calculate the lenght of the escaped version of `s`.

    Only backslashes and quotes will be escaped.

    Args:
      s (string)

    Returns:
      int: The lenght of the escaped string

    Examples:
      >>> escaped_len(r"")  # r'""'
      2
      >>> escaped_len(r"abc")  # r'"abc"'
      5
      >>> escaped_len(r"aaa\"aaa")  # r'"aaa\\\"aaa"'
      12
      >>> escaped_len(r"\x27")  # r'"\\x27"'
      7

    """
    # adding two for the enclosing quotes
    return len(s) + s.count('"') + s.count('\\') + 2


def main():
    import sys

    difference1 = difference2 = 0

    with open(sys.argv[1]) as f:
        for line in f:
            difference1 += len(line) - unescaped_len(line)
            difference2 += escaped_len(line) - len(line)

    print(difference1)
    print(difference2)


if __name__ == '__main__':
    main()
