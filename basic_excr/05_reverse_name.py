# Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
# Ex:  Input your name: Harash Rajput
#      Output: Rajput Harash


def reverse_full_name(full_name: str = "John Doe") -> str:
    """
    Docstring for reverse_full_name

    - param full_name: Provide full name eg. "John Doe"
    - type full_name: str
    - return: "Doe John"
    - rtype: str
    """
    name_chunk_reversed = full_name.split(" ")[::-1]
    reversed_full_name = " ".join(name_chunk_reversed)
    return reversed_full_name


name = input("Enter Your Name: ")
reversed_name = reverse_full_name(full_name=name)
print("Reversed Name", reversed_name)
