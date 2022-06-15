n = list(map(str, input().split()))
max = 0
min = 99999999999999
n = list(set(n))
n.sort()
for i in n:
    if len(i) > max:
        max = len(i)
    if len(i) < min:
        min = len(i)
for i in n:
    if len(i) == max:
        print(i, max)
for i in n:
    if len(i) == min:
        print(i, min)
