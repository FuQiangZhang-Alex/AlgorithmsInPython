
import math


class Point:
    def __init__(self, x=0, y=0, angle=None):
        self.x = x
        self.y = y
        self.angle = angle

    def distance(self, p):
        if not isinstance(p, Point):
            return None
        return math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)
        # square = [(i - j) ** 2 for i, j in zip(self, p)]

    def __str__(self):
        return str('(' + str(self.x) + ', ' + str(self.y) + ') ' + str(self.angle))


def calculate_angle(points):
    points_lst = list(points)
    points_lst.sort(key=lambda pt: pt.y, reverse=True)
    low = points_lst.pop()
    for point in points_lst:
        x0 = low.x
        y0 = low.y
        x1, y1 = point.x, point.y
        angle = None
        if y0 == y1:
            if x1 > x0:
                point.angle = 90
            elif x1 < x0:
                point.angle = -90
            else:
                points_lst.remove(point)
                continue
        else:
            tan = (x0 - x1) / (y0 - y1)
            point.angle = math.atan(tan) * 180 / math.pi
    points_angle = list(sorted(points_lst, key=lambda p: p.angle, reverse=True))
    for pa in points_angle:
        print(pa)
    results = [points_angle[0], low, points_angle.pop()]
    points_angle.remove(points_angle[0])
    while points_angle:
        candidate_point = points_angle.pop()

input_points = (
    Point(1, 15),
    Point(11, 5),
    Point(4, 3),
    Point(-3, -6),
    Point(-10, 9),
    Point(4, 1),
    Point(-4, -5),
    Point(-3, 4)
)
calculate_angle(input_points)
