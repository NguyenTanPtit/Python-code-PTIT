import math

k, n = list(map(int, input().split()))
for i in range(k, n + 1):
    for j in range(i + 1, n + 1):
        for m in range(j + 1, n + 1):
            if math.gcd(i, j) == 1 and math.gcd(j, m) == 1 and math.gcd(i, m) == 1:
                print('(' + str(i) + ', ' + str(j) + ', ' + str(m) + ')')
