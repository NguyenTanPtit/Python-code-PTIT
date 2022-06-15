# số nguyên tố lớn nhất trong ma trận
import math


def check(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


n, m = list(map(int, input().split()))
a = []
count = 0
max_prime = 0
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if check(a[i][j]) and a[i][j] > max_prime:
            count += 1
            max_prime = a[i][j]
if count == 0:
    print('NOT FOUND')
else:
    print(max_prime)
    for i in range(n):
        for j in range(m):
            if a[i][j] == max_prime:
                print('Vi tri ['+str(i)+']['+str(j)+']')
