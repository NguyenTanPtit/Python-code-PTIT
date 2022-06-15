def sum(n):
    s = str(n)
    sum = 0
    for i in s:
        sum += int(i)
    return sum


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    tmp = 0
    for i in range(0, n, 1):
        for j in range(i, n, 1):
            if sum(a[i]) > sum(a[j]):
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp
            elif sum(a[i]) == sum(a[j]) and a[i] > a[j]:
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp
    for i in a:
        print(i, end=" ")
    print()
