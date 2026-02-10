# Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.

def rule_checker_five(n1: int, n2: int) -> bool:
    if n1 == n2:
        return True
    elif abs(n1-n2) == 5:
        return True
    elif (n1+n2) ==5:
        return True
    return False

print(rule_checker_five(7, 2))
print(rule_checker_five(3, 2))
print(rule_checker_five(2, 2))
print(rule_checker_five(7, 3))
print(rule_checker_five(27, 53))