# dãy con chung của 3 dãy số
t = int(input())
while t > 0:
    t -= 1
    res = ''
    check, m1, m2, m3 = 0, 0, 0, 0
    a, b, c = list(map(int, input().split()))
    s1 = list(map(int, input().split()))
    s2 = list(map(int, input().split()))
    s3 = list(map(int, input().split()))
    while m1 < a and m2 < b and m3 < c:
        if s1[m1] == s2[m2] == s3[m3]:
            res += str(s1[m1]) + " "
            check = 1
            m1, m2, m3 = m1 + 1, m2 + 1, m3 + 1
        elif s1[m1] < s2[m2]:
            m1 += 1
        elif s2[m2] < s3[m3]:
            m2 += 1
        else:
            m3 += 1
    if check == 0:
        print('NO')
    else:
        print(res)
