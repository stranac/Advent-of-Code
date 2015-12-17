#!/usr/bin/env python3
"""Day 17: No Such Thing as Too Much

The elves bought too much eggnog again - 150 liters this time.To fit it all
into your refrigerator, you'll need to move it into smaller containers.
You take an inventory of the capacities of the available containers.

Filling all containers entirely, how many different combinations of
containers can exactly fit all 150 liters of eggnog?

Part 2:
Find the minimum number of containers that can exactly fit all 150 liters of
eggnog. How many different ways can you fill that number of containers and
still hold exactly 150 litres?

"""


def container_combinations(containers, goal, used=()):
    """Find all ways to combine the available containers to a
    total of `goal` units of storage.

    Args:
      containers (tuple of ints): Available containers.
      goal (int): Needed amount of storage.

    Yields:
      int: Possible combinations.

    Examples:

      >>> list(container_combinations((20, 15, 10, 5, 5), 25))
      [(20, 5), (20, 5), (15, 10), (15, 5, 5)]

    """
    if goal == 0:
        yield used

    else:
        for i, container in enumerate(containers):
            if container <= goal:
                yield from container_combinations(
                    containers[i + 1:],
                    goal - container,
                    used + (container,)
                )


def main():
    import sys

    with open(sys.argv[1]) as f:
        containers = tuple(int(line) for line in f)

    all_combinations = list(container_combinations(containers, 150))
    shortest = min(len(comb) for comb in all_combinations)

    print(len(all_combinations))
    print(sum([1 for comb in all_combinations if len(comb) == shortest]))


if __name__ == '__main__':
    main()
