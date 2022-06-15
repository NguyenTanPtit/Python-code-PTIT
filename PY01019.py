t = int(input())
while t > 0:
    s = input()
    s1 = list(s)
    s1.reverse()
    check = True
    for i in range(1, len(s), 1):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(s1[i]) - ord(s1[i - 1])):
            check = False
            break
    if check:
        print('YES')
    else:
        print('NO')
    t -= 1
