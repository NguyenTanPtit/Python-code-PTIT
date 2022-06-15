# bảng điểm


class Student:

    def __init__(self, id, name, line):
        self.id = format("HS%02d" % id)
        self.name = name
        score = list(map(float, line.split()))
        self.toan = score[0]
        self.van = score[1]
        self.anh = score[2]
        self.ly = score[3]
        self.hoa = score[4]
        self.sinh = score[5]
        self.su = score[6]
        self.dia = score[7]
        self.congdan = score[8]
        self.congnghe = score[9]

    def average(self):
        return (self.toan * 2 + self.van * 2 + self.anh + self.ly +
                self.hoa + self.sinh + self.su + self.dia + self.congdan + self.congnghe) / 10 / 1.2

    def rank(self):
        if self.average() >= 9:
            return 'XUAT SAC'
        elif self.average() >= 8:
            return 'GIOI'
        elif self.average() >= 7:
            return 'KHA'
        elif self.average() >= 5:
            return 'TB'
        else:
            return 'YEU'

    def __str__(self):
        return self.id + " " + self.name + " " + str(round(self.average(), 1)) + " " + self.rank()

    def __eq__(self, other):
        return self.average() == other.average()

    def __lt__(self, other):
        if self.average() == other.average():
            return self.id < other.id
        return self.average() > other.average()


t = int(input())
student = []
id = 1
while t > 0:
    t -= 1
    student.append(Student(id, input(), input()))
    id += 1
student.sort()
for i in student:
    print(i)
