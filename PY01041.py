# số tăng giảm
t = int(input())
while t > 0:
    t -= 1
    n = input()
    if len(n) < 3:
        print('NO')
    else:
        res = 0
        check1 = False
        for i in range(len(n)):
            check2 = True
            for j in range(0, i-1):
                if n[j] >= n[j+1]:
                    check2 = False
                    break
            if not check2:
                continue
            for k in range(i, len(n)-1):
                if n[k] <= n[k+1]:
                    check2 = False
                    break
            if check2:
                check1 = True
                print('YES')
                break
        if not check1:
            print('NO')



