#!/usr/bin/env python3
"""Day 14: Reindeer Olympics

This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must
rest occasionally to recover their energy. Santa would like to know which of
his reindeer is fastest, and so he has them race.

Reindeer can only either be flying (always at their top speed) or
resting (not moving at all), and always spend whole seconds in either state.

What is the longest distance traveled by a reindeer after a given time?

Part 2:
At the end of each second, Santa awards one point to the reindeer currently
in the lead. What is the score of the winning reindeer?

"""
import re
import itertools


class Reindeer:
    def __init__(self, speed, travels, rests):
        self.speed = speed
        self.travels = travels
        self.cycle_duration = travels + rests

        self.score = 0
        self.traveled = 0

    @classmethod
    def from_string(cls, line):
        """Create a reindeer from a string containing its speed, flight time,
        and rest time.

        Args:
          line (str): A line containing the reindeer's data, in format:
            <name> can fly <speed> km/s for <flight time> seconds,
            but then must rest for <rest time> seconds.

        """
        data = [int(number) for number in re.findall(r'\d+', line)]
        return cls(*data)

    def flying(self, time):
        """Determine if the reindeer is flying.

        Args:
          time (int): Current race duration in seconds.

        Returns:
          bool: True if the reindeer is flying, False otherwise

        """
        return (time % self.cycle_duration) < self.travels

    def move(self, time):
        """Move the reindeer if it is flying.

        Args:
          time (int): Current race duration in seconds.

        """
        if self.flying(time):
            self.traveled += self.speed


def distance_traveled(speed, travels, rests, total_time):
    """Calculate the distance the reindeer has flied in `total_time` seconds.

    Args:
      speed (int): The reindeer's speed in km/s.
      travels (int): The number of seconds the reindeer can fly before resting.
      rests (int): The number of seconds the reindeer needs to rest.
      total_time (int): The time the reindeer has for his travel.

    Returns:
      int: Traveled distance in km.

    Examples:
      >>> distance_traveled(14, 10, 127, 1000)
      1120
      >>> distance_traveled(16, 11, 162, 1000)
      1056

    """
    full_cycles, time_left = divmod(total_time, travels + rests)
    return (full_cycles * travels + min(time_left, travels)) * speed


def leaders(herd):
    """Get the reindeer who are currently in the lead.

    Args:
      herd (list): A list of all reindeer.

    Returns:
      An iterator of the reindeer currently in the lead.

    """
    herd = sorted(herd, key=lambda d: d.traveled, reverse=True)
    leader_score = herd[0].traveled
    return itertools.takewhile(lambda d: d.traveled == leader_score, herd)


def main():
    import sys

    with open(sys.argv[1]) as f:
        herd = [Reindeer.from_string(line) for line in f]

    for time in range(int(sys.argv[2])):
        for deer in herd:
            deer.move(time)
        for leader in leaders(herd):
            leader.score += 1

    print(max(deer.traveled for deer in herd))
    print(max(deer.score for deer in herd))


if __name__ == '__main__':
    main()
