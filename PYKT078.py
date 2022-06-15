# sắp xếp dãy số
t = int(input())
while t > 0:
    t -= 1
    a = []
    d = []
    n, m = list(map(int, input().split()))
    s = list(map(int, input().split()))
    for i in s:
        if i < 0:
            a.append(i)
        else:
            d.append(i)
    k = d[:]
    k.sort()
    res = 0
    for i in range(0, len(k)):
        if d[i] == k[len(k) - 1]:
            d.insert(i, m)
            break
    print(*a, end=" ")
    print(*d)
