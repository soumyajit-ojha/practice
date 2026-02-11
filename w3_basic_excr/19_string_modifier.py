# Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front.
# Return the string unchanged if the given string already begins with "Is".

def str_modifier(st: str) -> str:
    return "ls" + st

st = "Apple is red."
res = str_modifier(st)
print(res)
