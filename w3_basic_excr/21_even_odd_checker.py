# Write a Python program that determines whether a given number (accepted from the user) is even or odd,
# Prints an appropriate message to the user.


def even_checker(n: int | float) -> bool:
    print(type(n))
    if not isinstance(n, (int, float)):
        raise TypeError("Support intreger or float value only.")
    if n % 2 == 0:
        return True
    return False


num = eval(input("Enter number: "))

if even_checker(n=num):
    print("Even")
else:
    print("Odd")
