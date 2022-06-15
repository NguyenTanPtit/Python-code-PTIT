t = int(input())
while t > 0:
    n = int(input())
    s = input()
    x = input()
    d = list(map(int, s.split()))
    d1 = list(map(int, x.split()))
    d.sort()
    d1.sort()
    check = True
    for i in range(n):
        if d[i] > d1[i]:
            check = False
            break
    if check:
        print("YES")
    else:
        print("NO")
    t -= 1
