# Write a Python program to find the least common multiple (LCM) of two positive integers.


def gdc(n1: int, n2: int) -> int | float:
    deviser = min(n1, n2)
    dividend = max(n1, n2)
    while dividend % deviser != 0:
        reminder = dividend % deviser
        dividend = deviser
        deviser = reminder
    return deviser


def lcm(n1: int, n2: int) -> int:
    lcm = (n1 * n2) / gdc(n1, n2)
    return lcm


res = lcm(12, 18)
print(res)
