# hệ cơ số 3
t = int(input())
while t > 0:
    t -= 1
    n = input()
    check = True
    for i in n:
        if i != '0' and i != '1' and i != '2':
            check = False
            break
    if check:
        print('YES')
    else:
        print('NO')

