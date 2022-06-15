def check(n):
    s = str(n)
    s1 = s[::-1]
    if s1 != s or len(s) % 2 != 0:
        return False
    for i in s:
        if int(i) % 2 != 0:
            return False
    return True


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    s = ''
    for i in range(22, n, 22):
        if check(i):
            print(i, end=" ")
    print()
