# Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).


def point_distance(p1: tuple[int], p2: tuple[int]) -> int | float:
    x1, y1 = p1
    x2, y2 = p2

    delta_x = x2 - x1
    delta_y = y2 - y1

    distance = ((delta_x**2) + (delta_y**2)) ** 0.5
    return distance


point_1 = (4, 0)
point_2 = (6, 6)
dis = point_distance(p1=point_1, p2=point_2)
rounded_distance = round(dis, 2)

print(rounded_distance)
