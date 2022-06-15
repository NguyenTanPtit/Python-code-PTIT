while True:
    s = list(map(int, input().split()))
    if s.count(0) == 4:
        break
    dem = 0
    while True:
        if s.count(0) == 4:
            break

        x = s[0]
        for i in range(0, 3, 1):
            s[i] = abs(s[i] - s[i + 1])
        s[3] = abs(s[3] - x)
        dem += 1
    print(dem - 1)
