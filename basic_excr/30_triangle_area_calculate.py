# Write a Python program that will accept the base and height of a triangle and compute its area.
from decimal import Decimal


def triangle_area_calculate(base: float, height: float) -> float:
    if not isinstance(base, (int | float)):
        raise TypeError("base length must be a decimal or integer value")

    if not isinstance(height, (int | float)):
        raise TypeError("height length must be a decimal or integer value")

    base = Decimal(str(base))
    height = Decimal(str(height))
    area = (base * height) / 2
    return area


base = 10.20
height = 40
area = triangle_area_calculate(base=base, height=height)
print(area)
