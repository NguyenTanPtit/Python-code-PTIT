def check(n):
    s = str(n)
    for i in range(len(s)):
        if int(s[i]) != 4 and int(s[i]) != 7:
            return False
    return True


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    if check(n):
        print('YES')
    else:
        print('NO')
