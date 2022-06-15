t = int(input())
while t > 0:
    t -= 1
    s = input()
    s = list(s)
    count = 0
    for i in range(len(s) - 1, 0, -1):
        if int(s[i]) < int(s[i - 1]):
            temp = s[i]
            s[i] = s[i - 1]
            s[i - 1] = temp
            count += 1
            break
    if count == 1 and s[0] != '0':
        for i in s:
            print(i, end='')
        print()
    else:
        print(-1)
