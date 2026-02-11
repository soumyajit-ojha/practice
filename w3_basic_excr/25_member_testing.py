# Write a Python program that checks whether a specified value is contained within a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False


def is_group_member(group_data: list | tuple, value: int | float | str) -> bool:
    return value in group_data


data_set = [1, 5, 8, 3]
data = -1
res = is_group_member(group_data=data_set, value=data)
print(res)
