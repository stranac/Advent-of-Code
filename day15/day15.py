#!/usr/bin/env python3
"""Day 15: Science for Hungry People

Today, you set out on the task of perfecting your milk-dunking cookie recipe.
All you have to do is find the right balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a
list of the remaining ingredients you could use to finish the recipe
(your puzzle input) and their properties per teaspoon.

Given the ingredients in your kitchen and their properties, what is the total
score of the highest-scoring cookie you can make?

Part 2:
Given the ingredients in your kitchen and their properties, what is the total
score of the highest-scoring cookie you can make with a calorie total of 500?

"""
import re

import operator
import functools

INT_RE = r'-?\d+'


def tuples_with_sum(target, lenght):
    """Find tuples of `lenght` elements with the total sum of `target`.

    Args:
      target (int): Target sum.
      lenght (int): Wanted result lenght.

    Yields:
      Tuples of `lenght` elements.

    Examples:
      >>> list(tuples_with_sum(4, 2))
      [(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)]

    """
    if lenght == 1:
        yield (target,)
    else:
        for n in range(target + 1):
            for result in tuples_with_sum(target - n, lenght - 1):
                yield result + (n,)


@functools.lru_cache()
def cookie_score(counts, ingredients, calories=None):
    """Calculate the score of a cookie.

    The total score of a cookie can be found by adding up each of the
    properties (negative totals become 0) and then multiplying together
    everything except calories.

    If `calories` is not `None`, and the calorie total of the cookie isn't
    equal to `calories`, returns 0.

    Args:
      counts (tuple of ints): Amounts of each ingredient.
      ingredients (tuple of tuples): Properties of each ingredient.
      calories (int or None): Target amount of calories.

    Returns:
      int: Cookie score

    Examples:
      >>> counts = (44, 56)
      >>> ingredients = ((-1, -2, 6, 3, 8), (2, 3, -2, -1, 3))
      >>> cookie_score(counts, ingredients)
      62842880

    """
    *values, calorie_count = score_factors(counts, ingredients)
    if calories is not None and calorie_count != calories:
        return 0
    return product(values)


def score_factors(counts, ingredients):
    """Calculate total capacity, durability, flavor, texture and calories
    of a cookie.

    Args:
      counts (tuple of ints): Amounts of each ingredient.
      ingredients (tuple of tuples): Properties of each ingredient.

    Returns:
      A list of [capacity, durability, flavor, texture, calories]

    """

    factors = [0] * 5
    for count, ingredient in zip(counts, ingredients):
        for i, value in enumerate(ingredient):
            factors[i] += count * value
    return [max(factor, 0) for factor in factors]


def product(values):
    """Calculate the product of the numbers in `values`.

    Args:
      values (list of numbers)

    Returns:
      Product of the numbers

    """
    return functools.reduce(operator.mul, values)


def main():
    import sys

    with open(sys.argv[1]) as f:
        # need immutable args for functools.lru_cache
        ingredients = tuple(
            tuple(int(n) for n in re.findall(INT_RE, line)) for line in f
        )

    all_counts = list(tuples_with_sum(100, len(ingredients)))

    print(max(cookie_score(counts, ingredients) for counts in all_counts))
    print(max(cookie_score(counts, ingredients, 500) for counts in all_counts))


if __name__ == '__main__':
    main()
