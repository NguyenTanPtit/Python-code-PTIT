class Student:
    def __init__(self, line):
        s = list(map(str, line.split()))
        self.name = s[0]
        self.score = int(s[1])

    def __str__(self):
        return self.name

    def __lt__(self, other):
        if self.score == other.score:
            return self.name > other.name
        return self.score < other.score


n, k = list(map(int, input().split()))
if n > 70 or k > 5 or k > n:
    print('INVALID INPUT')
else:
    st = []
    while n > 0:
        n -= 1
        st.append(Student(input()))
    st.sort()
    for i in range(len(st) -1, len(st)-1-k, -1):
        print(st[i], end=" ")
