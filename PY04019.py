# Tuyển nhân viên
class Staff:
    def __init__(self, id, name, lythuyet, thuchanh):
        self.id = format("TS%02d" % id)
        self.name = name
        if float(lythuyet) > 10:
            self.lythuyet = lythuyet[0] + '.' + lythuyet[1:]
        else:
            self.lythuyet = lythuyet
        if float(thuchanh) > 10:
            self.thuchanh = thuchanh[0] + '.' + thuchanh[1:]
        else:
            self.thuchanh = thuchanh

    def average(self):
        return (float(self.lythuyet) + float(self.thuchanh)) / 2

    def rank(self):
        if self.average() < 5:
            return 'TRUOT'
        elif self.average() < 8:
            return 'CAN NHAC'
        elif self.average() <= 9.5:
            return 'DAT'
        else:
            return 'XUAT SAC'

    def __lt__(self, other):
        return self.average() > other.average()

    def __str__(self):
        return str(self.id) + " " + self.name + " " + str(format("%.2f" % round(self.average(), 2)))+" "+self.rank()


t = int(input())
staff = []
id = 1
while t > 0:
    t -= 1
    staff.append(Staff(id, input(), input(), input()))
    id += 1
staff.sort()
for i in staff:
    print(i)

# 6.039
# 5.6
# 4.365
