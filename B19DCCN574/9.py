# lớp tam giác vuông
class Tamgiac:
    def __init__(self, line):
        s = list(map(int, line.split()))
        self.a = s[0]
        self.b = s[1]
        self.c = s[2]

    def isRectangle(self):
        n = max(self.a, self.b, self.c)
        if self.a ** 2 + self.b ** 2 == n**2 or self.a ** 2 + self.c ** 2 == n**2 or self.c + self.b == n**2:
            return True
        return False

    def chuvi(self):
        return self.a + self.b + self.c

    def dientich(self):
        n = max(self.a, self.b, self.c)
        if self.a == n:
            return 0.5*(self.b*self.c)
        elif self.b == n:
            return 0.5*(self.a*self.c)
        else:
            return 0.5*self.a*self.b


s = input()
tamgiac = Tamgiac(s)
if tamgiac.isRectangle():
    print(str(int(tamgiac.chuvi()))+" "+str(int(tamgiac.dientich())))
else:
    print('INVALID')
