# Write a Python program to test whether a number is within 100 of 1000 or 2000.


def number_range(n: float | int) -> str:
    if  n <= 100:
        return f"below 100"
    elif 100 < n <= 1000:
        return f"101 - 1000"
    elif 1001 < n <= 2000:
        return f"1001 - 2000"
    else:
        return None


num = eval(input("Enter number: "))
res = number_range(num)
print("The available range is", res)
