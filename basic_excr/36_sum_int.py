# Write a Python program to add two objects if both objects are integers.


def sum_int(obj1, obj2):
    if isinstance(obj1, int) and isinstance(obj2, int):
        return obj1 + obj2
    
    return "Required \"int\" object only."


print(sum_int(10, 20))
print(sum_int(10, 20.23))
print(sum_int("5", 6))
print(sum_int("5", "6"))
