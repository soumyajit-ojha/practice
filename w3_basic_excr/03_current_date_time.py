# Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

from datetime import datetime

# datetime.now() -> return -> 2026-02-08 12:31:31.017472
now = datetime.now()
print(f"The current date and time is: \n{now}")
formated_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted time : {formated_time}")
formated_time = now.strftime("%y-%m-%d %H:%M:%S")
print(f"Formatted time : {formated_time}")

"""
NOTE:
=== %Y vs %y ===
%Y (Uppercase): Displays the four-digit year (e.g., 2026).
%y (Lowercase): Displays the two-digit year (e.g., 26).

=== %h vs %H ===
%h (Lowercase): This is actually a shortcut for the month name (e.g., Feb). It does not represent hours.
%H (Uppercase): Displays the hour in 24-hour format (00 to 23).

=== %m:%s vs %M:%S ===
%m (Lowercase): Displays the month as a number (01 to 12).
%M (Uppercase): Displays the minute (00 to 59).

%s (Lowercase): This is not a standard Python strftime code for seconds; it will likely print the literal character "s" or the Unix timestamp depending on your platform.
%S (Uppercase): Displays the second (00 to 59).

%D = month/date/year
"""

