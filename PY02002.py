fi = [1, 1, 2]
for i in range(3, 94):
    fi.append(fi[i - 1] + fi[i - 2])
t = int(input())
while t > 0:
    a, b = list(map(int, input().split()))
    for i in range(a - 1, b):
        print(fi[i], end=' ')
    print()
    t -= 1
