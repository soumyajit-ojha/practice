# Write a Python program to create a histogram from a given list of integers.


def create_histogram(data_list: list[int]) -> str:
    printed_char = "@"
    output = ""
    if not isinstance(data_list, (list, tuple, set)):
        raise TypeError(
            "Histogram must requred a collection of integers not a",
            str(type(data_list)),
        )
    for i in data_list:
        if not output:
            output += printed_char * i
        else:
            output += "\n" + (printed_char * i)
    return output


nums = [2, 3, 6, 5]
res = create_histogram(data_list=nums)
print(res)
