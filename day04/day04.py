#!/usr/bin/env python3
"""Day 4: The Ideal Stocking Stuffer

Santa needs help mining some AdventCoins (very similar to bitcoins) to use as
gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at
least five zeroes. The input to the MD5 hash is some secret key
(your puzzle input, given below) followed by a number in decimal.
To mine AdventCoins, you must find Santa the lowest positive number
(no leading zeroes: `1`, `2`, `3`, ...) that produces such a hash.

Examples:
  If your secret key is `abcdef`, the answer is `609043`, because the MD5 hash
  of `abcdef609043` starts with five zeroes (`000001dbbfa...`), and it is the
  lowest such number to do so.

  If your secret key is `pqrstuv`, the lowest number it combines with to make
  an MD5 hash starting with five zeroes is `1048970`;
  that is, the MD5 hash of `pqrstuv1048970` looks like `000006136ef....`

Part 2: find one that starts with six zeroes.

"""
import hashlib
import itertools

KEY = 'bgvyzdsv'


def main():
    for i in itertools.count():
        code = '{}{}'.format(KEY, i)
        hashed = hashlib.md5(code.encode('ascii')).hexdigest()
        if hashed.startswith('0' * 5):
            print(i)
        if hashed.startswith('0' * 6):
            print(i)
            break


if __name__ == '__main__':
    main()
