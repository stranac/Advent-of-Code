#!/usr/bin/env python3
"""Day 2: I Was Told There Would Be No Math

The elves are running low on wrapping paper, and so they need to submit
an order for more. They have a list of the dimensions
(length `l`, width `w`, and height `h`) of each present,
and only want to order exactly as much as they need.

The elves are also running low on ribbon. Ribbon is all the same width, so
they only have to worry about the length they need to order, which they
would again like to be exact.

The ribbon required to wrap a present is the shortest distance around its
sides, or the smallest perimeter of any one face. Each present also requires
a bow made out of ribbon as well; the feet of ribbon required for the
perfect bow is equal to the cubic feet of volume of the present.

"""

import functools
import operator


def product(values):
    """Calculate the product of the numbers in `values`.

    Args:
      values (list of numbers)

    Returns:
      Product of the numbers

    """
    return functools.reduce(operator.mul, values)


def surface_area(dimensions):
    """Calculate the surface area of a box.

    Args:
      dimensions (list of int): Box dimensions

    Returns:
      int: Box surface area

    """
    a, b, c = dimensions
    return 2 * (a * b + a * c + b * c)


def perimeter(dimensions):
    """Calculate the perimeter of a side.

    Args:
      dimensions (list of int): Side dimensions

    Returns:
      int: Side perimeter

    """
    a, b = dimensions
    return 2 * (a + b)


def main():
    paper_needed = 0
    ribbon_needed = 0

    with open('input') as f:
        for line in f:
            # sort the sides so it's easy to get the two smallest
            sides = sorted(map(int, line.split('x')))

            paper_needed += surface_area(sides) + product(sides[:2])
            ribbon_needed += perimeter(sides[:2]) + product(sides)

    print(paper_needed)
    print(ribbon_needed)


if __name__ == '__main__':
    main()
