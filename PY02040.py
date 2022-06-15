# ma trận 2
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
sumduoi = 0
sumtren = 0
for i in range(n):
    for j in range(n):
        if i < n - j - 1 and j < n - i - 1:
            sumtren += a[i][j]
        elif j == (n - i - 1):
            continue
        else:
            sumduoi += a[i][j]

k = int(input())
if abs(sumtren - sumduoi) > k:
    print('NO')
else:
    print('YES')
print(str(abs(sumtren - sumduoi)))
