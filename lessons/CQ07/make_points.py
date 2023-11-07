from lessons.CQ07.point import Point

my_point: Point = Point(2.4, 5.8)
print(Point)
print(my_point.x)

my_point.scale_by(2)
print(my_point.x)

new_point: Point = my_point.scale(4)
print(new_point.x)
