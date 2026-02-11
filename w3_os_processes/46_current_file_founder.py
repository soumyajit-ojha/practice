# Write a Python program to retrieve the path and name of the file currently being executed.

import os

# current file name
print("PATH ",os.path.abspath(__file__))

