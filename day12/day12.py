#!/usr/bin/env python3
"""Day 12: JSAbacusFramework.io

Santa's Accounting-Elves need help balancing the books after a recent order.
Unfortunately, their accounting software uses a peculiar storage format.

They have a JSON document which contains a variety of things:
arrays (`[1,2,3]`), objects (`{"a":1, "b":2}`), numbers, and strings.
Your first job is to simply find all of the numbers throughout the document
and add them together.

Part 2:
The Accounting-Elves have realized that they double-counted everything red.
Ignore any object (and all of its children) which has any property
with the value "red".

"""
import json


def all_nums(data, ignore_reds=False):
    """Get all the integer values from `data`.

    If `ignore_reds` is set, any dicts containing the value 'red' are ignored.

    Args:
      data (loaded json structure)
      ignore_reds (bool)

    Yields:
      int: Integer values inside `data`.

    """
    if isinstance(data, int):
        yield data

    elif isinstance(data, list):
        for value in data:
            yield from all_nums(value, ignore_reds)

    elif isinstance(data, dict):
        if ignore_reds and 'red' in data.values():
            return
        for value in data.values():
                yield from all_nums(value, ignore_reds)


def main():
    with open('input') as f:
        data = json.load(f)

    print(sum(all_nums(data)))
    print(sum(all_nums(data, ignore_reds=True)))


if __name__ == '__main__':
    main()
