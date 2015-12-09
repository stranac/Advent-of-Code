#!/usr/bin/env python3
"""Day 9: All in a Single Night

Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided
him the distances between every pair of locations. He can start and end at any
two (different) locations he wants, but he must visit each location exactly
once. What is the shortest distance he can travel to achieve this?

Part 2 - What is the distance of the longest route?

"""
from collections import defaultdict
from itertools import permutations


def path(towns, distances):
    """Calculate the total distance by going through each of the towns.

    Args:
      towns (tuple): Towns we're going through.
      distances (dict of dict): Mapping the distance between each two cities.

    Returns:
      int: The total distance

    Examples:
    >>> distances = {
        'London': {
            'Dublin': 464,
            'Belfast': 518,
        },
        'Dublin': {
            'London': 464,
            'Belfast': 141,
        },
        'Belfast': {
            'London': 518,
            'Dublin': 141,
        },
    }
    >>> path('Dublin', 'London', 'Belfast')
    982
    >>> path('London', 'Dublin', 'Belfast')
    605
    >>> path('London', 'Belfast', 'Dublin')
    659
    >>> path('Dublin', 'Belfast', 'London')
    659
    >>> path('Belfast', 'Dublin', 'London')
    605
    >>> path('Belfast', 'London', 'Dublin')
    982

    """
    distance = 0
    for town1, town2 in zip(towns, towns[1:]):
        distance += distances[town1][town2]
    return distance


def main():
    distances = defaultdict(dict)
    with open('input') as f:
        for line in f:
            pair, distance = line.split(' = ')
            town1, town2 = pair.split(' to ')
            distances[town1][town2] = int(distance)
            distances[town2][town1] = int(distance)

    all_paths = [path(towns, distances) for towns in permutations(distances)]

    print(min(all_paths))
    print(max(all_paths))

if __name__ == '__main__':
    main()
