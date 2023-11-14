"""Makes a point using Point class."""

from lessons.CQ07.point import Point

my_point: Point = Point(2.4, 5.8)
print(Point)
print(my_point.x)

my_point.scale_by(2)
print(my_point.x)

new_point: Point = my_point * 2.0
other_point: Point = Point()

print(my_point)
print(new_point)
print(other_point)
