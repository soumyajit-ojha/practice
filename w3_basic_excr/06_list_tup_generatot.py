# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')


def tuple_generator(input_data: str, separator: str = ",") -> tuple:
    if "," not in input_data:
        return "Provide the separator"
    value_list = input_data.split(",")
    return tuple(value_list)


def list_generator(input_data: str, separator: str = ",") -> tuple:
    if "," not in input_data:
        return "Provide the separator"
    return input_data.split(",")


def list_tuple_creater(input_data: str, separator: str = ",") -> list | tuple | str:
    tup = tuple_generator(input_data=input_data, separator=separator)
    list = list_generator(input_data=input_data, separator=separator)
    return tup, list


user_data = input("Data: ")
tup, lst = list_tuple_creater(user_data)
print(tup, lst)
