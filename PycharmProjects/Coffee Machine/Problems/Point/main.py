import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point):
        x_dist = self.x - point.x
        y_dist = self.y - point.y
        return math.sqrt(x_dist ** 2 + y_dist ** 2)
