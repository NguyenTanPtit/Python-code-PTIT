# DÃY SỐ PHÙ HỢP
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    check = True
    for i in range(n):
        if a[i] > b[i]:
            check = False
    if check:
        print('YES')
    else:
        print('NO')
