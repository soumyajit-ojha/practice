# Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum


def triple_sum(n1, n2, n3):
    if n1 == n2 == n3:
        return str(n1 * 3)
    else:
        return str(n1 + n2 + n3)


sum = triple_sum(10, 10, 10)
print("Triple sum:", sum)
