# Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

from datetime import date
d1=(2014, 2, 20)
d2=(2014, 3, 1)

first_date = date(*d1)
last_date = date(*d2)

diff =last_date-first_date
print(diff.days)
