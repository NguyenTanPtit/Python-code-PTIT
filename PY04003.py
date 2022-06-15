# Lớp phân số 1
import math


class Phanso:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rutgon(self):
        a = self.x / math.gcd(self.x, self.y)
        b = self.y / math.gcd(self.x, self.y)
        return Phanso(a, b)

    def __str__(self):
        return str(int(self.x)) + "/" + str(int(self.y))


a, b = list(map(int, input().split()))
print(Phanso(a, b).rutgon())
