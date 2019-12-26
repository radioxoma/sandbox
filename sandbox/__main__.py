#!/usr/bin/env python

import sys
import platform
import struct

print("Hello world from {}-bit {}".format(8 * struct.calcsize('P'), platform.system()))
print("Python version: {}".format(sys.version))
