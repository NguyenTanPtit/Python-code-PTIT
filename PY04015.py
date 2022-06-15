# LẬP HÓA ĐƠN - 1
class Bill:
    def __init__(self, id, name, old, new):
        self.id = format('KH%02d' % id)
        self.name = name
        self.old = old
        self.new = new

    def cs(self):
        return int(self.new) - int(self.old)

    def total(self):
        if self.cs() <= 50:
            return self.cs()* 100
        elif self.cs() <= 100:
            return 50*100 + (self.cs()-50)*150
        else:
            return 50 * 100 + 50*150 +(self.cs()-100)*200

    def phuThu(self):
        if self.cs() <= 50:
            return self.total()*0.02
        elif self.cs() <= 100:
            return self.total()*0.03
        else:
            return self.total()*0.05

    def Tongcong(self):
        return self.total() + self.phuThu()

    def __str__(self):
        return str(self.id)+" "+self.name+" "+str(int(round(self.Tongcong(), 0)))

    def __lt__(self, other):
        return self.Tongcong() > other.Tongcong()


t = int(input())
bill = []
id = 1
while t > 0:
    t -= 1
    bill.append(Bill(id, input(), input(), input()))
    id += 1
bill.sort()
for i in bill:
    print(i)
