n = int(input())
a = list(map(int, input().split()))
res = []
sums = 0
sum = 0
tich = 1
for i in range(len(a)):
    sums += a[i]
    tich *= sums
    res.append(sums)
for i in res:
    sum += i
print(sum, tich, sep=" ")
