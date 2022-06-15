# chia hết cho 7
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    if n % 7 == 0:
        print(n)
    else:
        check = True
        k = 0
        while n % 7 != 0:
            if k > 1000:
                check = False
                break
            n += int(str(n)[::-1])
            k += 1
        if check:
            print(n)
        else:
            print(-1)
