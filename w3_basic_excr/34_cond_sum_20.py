
# Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.


def conditional_sum(n1: int, n2: int) -> int:
    sum = n1 + n2
    if 15 <= sum <= 20:
        return 20
    return sum

print(conditional_sum(10, 6))
print(conditional_sum(10, 2))
print(conditional_sum(10, 12))