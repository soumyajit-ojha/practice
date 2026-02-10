# Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}

def unique_color_finder(list_1, list_2) -> set:
    unique_list_1 = set(list_1)
    unique_list_2 = set(list_2)

    unique_in_list_1 = unique_list_1 - unique_list_2
    return unique_in_list_1

l1 = ["White", "Black", "Red"]
l2 = ["Red", "Green"]
res = unique_color_finder(
    list_1=l1,
    list_2=l2
)

print(res)
