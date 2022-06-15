def check(u):
    if u < 2:
        return False
    for t in range(2, u):
        if u % t == 0:
            return False
    return True


n = input().split()
a = []
for i in range(0, int(n[0])):
    temp = []
    s = input().split()
    for j in range(len(s)):
        if check(int(s[j])):
            temp.append(1)
        else:
            temp.append(0)
    a.append(temp)
for i in range(0, int(n[0])):
    for j in range(0, int(n[1])):
        print(a[i][j], end=' ')
    print()
