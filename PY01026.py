# sắp đặt lại xâu kí tự
from collections import Counter

t = int(input())
k = 1
while t > 0:
    t -= 1
    check = True
    s1 = input()
    s2 = input()
    s1 = Counter(s1)
    s2 = Counter(s2)
    for i in s1:
        if s1[i] == s2[i]:
            continue
        else:
            check = False
            break
    if check:
        print('Test ' + str(k) + ': YES')
        k += 1
    else:
        print('Test ' + str(k) + ': NO')
        k += 1
