# Write a Python program that displays your name, age, and address on three different lines.


def personal_details(name: str, age: int, address: str) -> str:
    info = f"Name: {name}\nAge: {age}\nAddress: {address}"
    return info


data = personal_details(name="Soumyajit Ojha", age=24, address="Nagapur, Gop, Odisha")

print(data)
