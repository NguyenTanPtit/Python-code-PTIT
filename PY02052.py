# tính cân đối của ma trận 1
n = int(input())
a = []
sumtren = 0
sumduoi = 0
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if i > j:
            sumduoi += a[i][j]
        elif j > i:
            sumtren += a[i][j]
k = int(input())
if abs(sumtren - sumduoi) <= k:
    print('YES')
else:
    print('NO')
print(abs(sumtren - sumduoi))
