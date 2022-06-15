# triangle class
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def isTriangle(self):
        d1 = self.a.distance(self.b)
        d2 = self.b.distance(self.c)
        d3 = self.c.distance(self.a)
        if d1 + d2 > d3 and d1 + d3 > d2 and d3 + d2 > d1:
            return True
        return False

    def chuvi(self):
        d1 = self.a.distance(self.b)
        d2 = self.b.distance(self.c)
        d3 = self.c.distance(self.a)
        return format("%.3f" % (d1 + d2 + d3))


t = int(input())
while t > 0:
    t -= 1
    s = list(map(int, input().split()))
    a = Point(s[0], s[1])
    b = Point(s[2], s[3])
    c = Point(s[4], s[5])
    tg = Triangle(a, b, c)
    if tg.isTriangle():
        print(tg.chuvi())
    else:
        print('INVALID')

