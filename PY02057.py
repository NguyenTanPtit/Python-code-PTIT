# số may mắn trong ma trận
def check(n, a, b):
    if n == (a - b):
        return True
    return False


n, m = list(map(int, input().split()))
a = []
count = 0
max_prime = 0
for i in range(n):
    a.append(list(map(int, input().split())))
min = a[0][0]
max = a[0][0]
for i in range(n):
    for j in range(m):
        if a[i][j] < min:
            min = a[i][j]
        if a[i][j] > max:
            max = a[i][j]
for i in range(n):
    for j in range(m):
        if check(a[i][j], max, min) and a[i][j] > max_prime:
            count += 1
            max_prime = a[i][j]
if count == 0:
    print('NOT FOUND')
else:
    print(max_prime)
    for i in range(n):
        for j in range(m):
            if a[i][j] == max_prime:
                print('Vi tri [' + str(i) + '][' + str(j) + ']')
