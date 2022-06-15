t = int(input())
while t > 0:
    s = input()
    res = ''
    for i in range(1, len(s), 2):
        for j in range(0, int(s[i]), 1):
            res += s[i - 1]
    print(res)
    t -= 1
