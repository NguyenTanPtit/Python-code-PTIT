# # tính toán lượng mưa
class LuongMua:
    def __init__(self, id, name, time, mm):
        self.id = id
        self.name = name
        self.time = time
        self.mm = mm
        self.trungBinh = "%.2f" % round(self.mm/self.time*60, 2)


arrLuongMua = []
arrName = []
for i in range(int(input())):
    if i+1 < 10:
        id = "T0"+str(i+1)
    else:
        id = "T"+str(i+1)
    name = input()
    start = input().split(":")
    end = input().split(":")
    tongPhut = (int(end[0])*60+int(end[1]))-(int(start[0])*60+int(start[1]))
    mm = int(input())
    if name in arrName:
        for x in arrLuongMua:
            if x.name == name:
                tongPhut += x.time
                mm += x.mm
                id = x.id
                arrLuongMua.remove(x)
                arrLuongMua.append(LuongMua(id, name, tongPhut, mm))
                break
    else:
        arrName.append(name)
        arrLuongMua.append(LuongMua(id, name, tongPhut, mm))
ketQua = sorted(arrLuongMua, key=lambda i: i.id)
for x in ketQua:
    print(x.id, x.name, x.trungBinh)
