# Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years.
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79


def calculate_future_value(
    ammount: float | int, interest_percentage: int | float, time: int | float
) -> float:
    future_value = ammount * ((1 + (0.01 * interest_percentage)) ** time)
    return round(future_value, 2)


res = calculate_future_value(ammount=10000, interest_percentage=3.5, time=7)

print(res)
