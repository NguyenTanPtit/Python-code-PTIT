n = int(input())
a = list(map(int, input().split()))
a.sort()
check = False
t = 0
for i in range(n - 1):
    if abs(a[i] - a[i + 1]) != 1:
        t = a[i]
        check = True
        break
    else:
        check = False
if check:
    print(t + 1)
else:
    print(a[n - 1] + 1)
