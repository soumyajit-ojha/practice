# Write a Python program to calculate the difference between a given number and 17.
# If the number is greater than 17, return twice the absolute difference.

def diff_from_17(num: int) -> int:
    diff = abs(17 - num)
    if num > 17:
        return str(2*diff)
    else:
        return diff

num = 22
res = diff_from_17(num=num)
print("Result =", res)

