# Write a Python program to get the volume of a sphere with radius six.

from math import pi

def sphere_volume(radious: float) -> float:
    volume = (4/3) * pi * (radious**3)
    return volume

r = eval(input("Enter radious of sphere: "))
res = sphere_volume(radious=r)
print(f"Volume of sphere is {res} Unit Cube")
