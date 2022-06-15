# kiểm tra số đẹp
t = int(input())
while t > 0:
    t -= 1
    n = input()
    a = n[0]
    b = n[1]
    check = True
    for i in range(0, len(n), 2):
        if n[i] != a:
            check = False
            break
    for i in range(1, len(n), 2):
        if n[i] != b:
            check = False
            break
    if check:
        print('YES')
    else:
        print('NO')
