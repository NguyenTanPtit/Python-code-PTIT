# bảng xếp hạng
class Student:

    def __init__(self, name, line):
        self.name = name
        score = list(map(int, line.split()))
        self.ac = score[0]
        self.sub = score[1]

    def __str__(self):
        return self.name+" "+str(self.ac)+" "+str(self.sub)

    def __lt__(self, other):
        if self.ac == other.ac:
            if self.sub == other.sub:
                return self.name < other.name
            return self.sub < other.sub
        return self.ac > other.ac


t = int(input())
student = []
while t > 0:
    t -= 1
    student.append(Student(input(), input()))
student.sort()
for i in student:
    print(i)
