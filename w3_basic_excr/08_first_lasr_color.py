# Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]


def get_first_last_color(colors: list) -> list:
    return [colors[0], colors[-1]]


color_list = ["Red", "Green", "White", "Black"]
res = get_first_last_color(colors=color_list)
print("Result", res)
