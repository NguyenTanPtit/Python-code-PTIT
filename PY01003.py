def Round(s, n):
    s = list(map(int, s))
    if n == 1:
        return s[0]
    for i in range(n - 1, 0, -1):
        if s[i] >= 5:
            s[i - 1] += 1
            s[i] = 0
        else:
            s[i] = 0
    s1 = ''
    for i in range(0, n, 1):
        s1 += str(s[i])
    return s1


t = int(input())
while t > 0:
    n = input()
    print(Round(n, len(n)))
    t -= 1
