# sắp xếp theo tích các chữ số
def mul(n):
    s = str(n)
    t = 1
    for i in s:
        t *= int(i)
    return t


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    tmp = 0
    for i in range(0, n, 1):
        for j in range(i, n, 1):
            if mul(s[i]) > mul(s[j]):
                tmp = s[i]
                s[i] = s[j]
                s[j] = tmp
            elif mul(s[i]) == mul(s[j]) and s[i] > s[j]:
                tmp = s[i]
                s[i] = s[j]
                s[j] = tmp
    for i in s:
        print(i, end=" ")
    print()

