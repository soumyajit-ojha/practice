# Write a Python program that prints the calendar for a given month and year.
# Note : Use 'calendar' module.

import calendar

def display_calender(year: int, month: int):
    if 1947 < year > 2099:
        return "Provide a predictable year"
    if 12 > month < 1:
        return "Month can't exceed 12 or less than 1"

    return calendar.month(year, month)

y = int(input("Input a year: "))
m = int(input("Input month : "))
res = display_calender(year=y, month=m)
print(res)
