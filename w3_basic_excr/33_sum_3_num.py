# Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.


def sum_three_num(n1: int, n2: int, n3: int) -> int:
    if n1 == n2 or n1 == n3 or n2 == n3:
        return 0
    return n1 + n2 + n3


print(sum_three_num(2, 1, 2))
print(sum_three_num(3, 2, 2))
print(sum_three_num(2, 2, 2))
print(sum_three_num(1, 2, 3))