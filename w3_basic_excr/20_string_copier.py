# Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
# Eg. st = "apple", copy = 3
#  output = appleappleapple


def string_copy(st: str, copies: int) -> str:
    n = int(copies)
    if n <= 0:
        return "provide positive integer"
    return st * n


s = input("Enter String: ")
n = input("No of copy: ")
res = string_copy(st=s, copies=n)
print(res)
