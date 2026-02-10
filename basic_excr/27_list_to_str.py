# Write a Python program that concatenates all elements in a list into a string and returns it.


def concatinate(data_list: list) -> str:
    lst = list(map(str, data_list))
    return "".join(lst)


lst = [1, 5, 12, 2, "apple"]
res = concatinate(data_list=lst)
print(res)
