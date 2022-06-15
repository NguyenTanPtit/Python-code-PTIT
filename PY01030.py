import math

n, k = list(map(int, input().split()))
p = 10 ** k
q = 10 ** (k - 1)
dem = 0
for i in range(q, p, 1):
    if math.gcd(i, n) == 1:
        print(i, end=" ")
        dem += 1
    if dem == 10:
        print()
        dem = 0
