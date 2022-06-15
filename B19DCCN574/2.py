# covid
t = int(input())
if t > 10 or t <= 0:
    print("INVALID INPUT")
else:
    while t:
        t -= 1
        a = int(input())
        dem = 1
        if a > 365 or a <= 0:
            print("INVALID INPUT")
        else:
            ck = a // 11
            dem = 2 ** ck
            print(dem - 1)
