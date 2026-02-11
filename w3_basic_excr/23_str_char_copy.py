# Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string.
# Return n copies of the whole string if the length is less than 2.


def prefix_str_copy(st: str, n: int) -> str:
    if not isinstance(n, int):
        raise TypeError("n must be a integer.")
    if len(st) < 2:
        return st * n
    return st[:2] * n


st = "apple"
n = 3
res = prefix_str_copy(st=st, n=n)
print(res)
