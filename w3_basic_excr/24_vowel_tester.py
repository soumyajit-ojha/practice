# Write a Python program to test whether a passed letter is a vowel or not.


def is_vowel(char: str) -> bool:
    if not isinstance(char, str):
        raise TypeError("Only string type required.")
    return char[0].lower() in "aeiou"


x = eval(input("Enter char: "))
print(is_vowel(x))
