# Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.

import platform
import struct


print(platform.architecture())
print(struct.calcsize("P"))