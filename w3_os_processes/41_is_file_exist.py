# Write a Python program to check whether a file exists.
import pathlib


def is_exist(path: str):
    path = pathlib.Path(path).exists()
    return path


path = "C:\\Users\\DELL\\Desktop\\practice\\README.md"
print(is_exist(path))
