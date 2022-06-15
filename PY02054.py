# biến đổi về ma trận vuông
n, m = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
if n > m:
    x = n - m
    for i in range(0, x):
        a.remove(a[i])
elif m > n:
    x = m - n
    for i in range(1, x+1):
        for j in a:
            del j[i]
for i in range(len(a)):
    for j in range(len(a)):
        print(a[i][j], end=' ')
    print()
