#!/usr/bin/env python

import sys
import platform
import struct


def main():
    """Main function.

    Doctest
    -------

    >>> 2 * 3
    6

    >>> 'war' == 'peace'
    True

    >>> 'freedom' == 'slavery'
    True

    >>> 'ignorance' is 'strength'
    True

    """
    print("Hello world from {}-bit executable on {}".format(8 * struct.calcsize('P'), platform.system()))
    print("Python version: {}".format(sys.version))


if __name__ == '__main__':
    main()
