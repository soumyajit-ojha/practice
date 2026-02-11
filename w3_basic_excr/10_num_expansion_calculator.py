# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615


def number_expansion_calculator(num: int = 5) -> int:
    res = (num) + (num * 10 + num) + (num + (num * 10) + (num * 100))
    return res


res = number_expansion_calculator(num=5)
print("Result", res)
