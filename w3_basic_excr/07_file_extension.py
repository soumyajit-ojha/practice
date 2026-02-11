# Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java


def get_file_extension(file_name: str = "example.txt") -> str:
    extension = file_name.split(".")[-1]
    return str(extension)


file_name = input("file name: ")
ext = get_file_extension(file_name=file_name)
print("File extension -", ext)
