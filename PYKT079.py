# điền số
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    s = list(map(int, input().split()))
    s = set(s)
    s = list(s)
    s.sort()
    k = s[-1] - s[0] - len(s) + 1
    print(k)
