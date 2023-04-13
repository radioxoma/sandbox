#!/usr/bin/env python

import platform
import struct
import sys


def main():
    """Dummy main function.

    Doctests
    --------

    >>> 2 * 3
    6

    >>> "war" == "peace"  # doctest: +SKIP
    True

    >>> "freedom" != "slavery"
    True
    """
    print(
        "Hello world from {}-bit executable on {}".format(
            8 * struct.calcsize("P"), platform.system()
        )
    )
    print("Python version: {}".format(sys.version))


if __name__ == "__main__":
    main()
