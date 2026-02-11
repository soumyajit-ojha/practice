# Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :
# r = 1.1
# Area = 3.80

from decimal import Decimal
from math import pi


def circle_area(radious: float) -> float:
    """
    - r : radious of the circle.
    """
    try:
        area = pi * (radious * radious)
        return area
    except Exception as e:
        return "Unable to calculate"


r = 1.1
area = circle_area(radious=r)
print("value 1", format(area, ".2f"))
print("value 2", round(area, 2))
print(f"Area of circle with radious {r} : {area:.2f}")
