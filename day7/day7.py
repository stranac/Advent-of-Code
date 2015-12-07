#!/usr/bin/env python3
"""Day 7: Some Assembly Required

This year, Santa brought little Bobby Tables a set of wires and bitwise logic
gates! Unfortunately, little Bobby is a little under the recommended
age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry
a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire
by a gate, another wire, or some specific value. Each wire can only get a
signal from one source, but can provide its signal to multiple destinations.
A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describe how to connect the parts together:
`x AND y -> z` means to connect wires `x` and `y` to an `AND` gate,
and then connect its output to wire `z`.

"""
import operator

OP = {
    'IDENTITY': lambda x: x,
    'NOT': lambda x: 65535 - x,
    'AND': operator.and_,
    'OR': operator.or_,
    'LSHIFT': operator.lshift,
    'RSHIFT': operator.rshift,
}


def parse_line(line):
    """Parse an instruction into a tuple of (function, args, destination).

    Args:
      line (string): An instruction in format '<operations> -> destination'
        'operations' is one of:
          'value'
          'NOT value'
          'value1 <BINARY_OPERATOR> value2' (AND | OR | LSHIFT | RSHIFT)

    Returns:
      tuple: (function, args, destination). Interpreted as::

          destination = function(*args)

    Examples:
      `123 -> x` means that the signal `123` is provided to wire `x`.
      >>> parse_line('123 -> x')
      (OP['IDENTITY'], ('123',), 'x')

      `x AND y -> z` means that the bitwise `AND` of wire `x` and wire `y`
        is provided to wire `z`.
      >>> parse_line('x AND y -> z')
      (OP['AND'], ('x', 'y'), 'z')

    """
    *operations, _, destination = line.strip().split()
    # simple assignment
    if len(operations) == 1:
        return OP['IDENTITY'], (operations[0],), destination
    # NOT operation
    elif len(operations) == 2:
        return OP['NOT'], (operations[1],), destination
    # binary opration
    else:
        return OP[operations[1]], (operations[0], operations[2]), destination


def emulate_circuit(instructions, names):
    """Execute instructions to calculate the value of `a`.

    Args:
      instructions (list of tuples): Instructions given by :func:`parse_line`.
      names (dict): name bindings for the circuit.

    Returns:
      int: Final value of `a`.

    """
    while 'a' not in names:
        for op, args, dest in instructions:
            if dest in names:
                continue
            args = [value(arg, names) for arg in args]
            # can only calculate if all the arg values are known
            if None not in args:
                names[dest] = op(*args)
    return names['a']


def value(arg, names):
    """Find the value of `arg`, if known.

    Args:
      arg (string): String of digits or a name
      names (dict): Known name bindings

    Returns:
      `int(arg)` if `arg` is a string of digits
      `names[arg]` if `arg` is a known name
      `None` otherwise

    Examples:
      >>> value('a', {})
      >>> value('44430', {})
      44430
      >>> value('a', {'a': 44430})
      44430

    """
    try:
        return int(arg)
    except ValueError:
        return names.get(arg)


def main():
    with open('input') as f:
        instructions = [parse_line(line) for line in f]

    answer1 = emulate_circuit(instructions, {})
    answer2 = emulate_circuit(instructions, {'b': answer1})

    print(answer1)
    print(answer2)


if __name__ == '__main__':
    main()
