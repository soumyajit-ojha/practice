# Write a Python program to locate Python site packages.

import site
import sysconfig

print(site.getsitepackages())
paths = sysconfig.get_path("purelib")#["purelib"]
print(paths)
