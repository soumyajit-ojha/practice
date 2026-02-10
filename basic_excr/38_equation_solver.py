# Write a Python program to solve (x + y) * (x + y).
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49


def equation_solver(x: float | int, y: float | int) -> float | int:
    if not isinstance(x, (float|int)) and not isinstance(x, (float|int)):
        return "X and Y must be 'int' or 'float'."
    res = (x + y) * (x + y)
    return res


x = eval(input("Ener X = "))
y = eval(input("Ener y = "))

res = equation_solver(x, y)
print(res)
