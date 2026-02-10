# Write a Python program to print all even numbers from a given list of numbers in the same order and stop printing any after 50 in the sequence.
# Sample numbers list :
# in fetch_even_range(num_list = [1, 2, 3, 100, 45, 42, 66])


def is_even(n: float | int) -> bool:
    if n % 2 == 0:
        return True
    return False


def fetch_even_range(num_list: list, limit_range: float | int = 10) -> list[int]:
    return [i for i in num_list if i <= limit_range and is_even(i)]


lst = [1, 2, 3, 50, 48, 32, 100, 45, 42, 66]
res = fetch_even_range(num_list=lst, limit_range=50)
print(res)
