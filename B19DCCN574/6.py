# từ điển
t = int(input())
s = {}
if t > 10:
    print('INVALID INPUT')
else:
    while t > 0:
        t -= 1
        a, b = list(map(str, input().split()))
        s[a] = b
    tich = 1
    tong = 0
    for i in s.values():
        if i.isnumeric():
            tich *= int(i)
            tong += int(i)
    print(str(tong)+" "+str(tich))
