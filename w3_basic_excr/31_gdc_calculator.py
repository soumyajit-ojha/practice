# Write a Python program that computes the greatest common divisor (GCD) of two positive integers.


def calculate_gdc(n1: int, n2: int) -> int | float:
    deviser = min(n1, n2)
    dividend = max(n1, n2)
    while dividend % deviser != 0:
        reminder = dividend % deviser
        dividend = deviser
        deviser = reminder
    return deviser


def gdc(n1: int, n2: int, *args):
    gdc = calculate_gdc(n1, n2)
    if not args:
        return gdc
    res = 0
    for i in args:
        res = calculate_gdc(gdc, i)
    return res


res = gdc(30, 20, 60)
print(res)
