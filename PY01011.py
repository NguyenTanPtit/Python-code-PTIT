def check(n):
    s = str(n)
    x = s[::-1]
    if len(s) % 2 != 0:
        return False
    if x != s: return False
    for i in range(len(s) - 1):
        if int(s[i]) % 2 != 0:
            return False
    return True


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    for i in range(22, n, 22):
        if check(i):
            print(i, end=' ')
    print()
