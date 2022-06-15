# tổng ước số
import math

prime = [True] * 2000000
res = []

t = int(input())
sums = 0
prime[0] = False
prime[1] = False
for i in range(2, int(math.sqrt(2000000))):
    if prime[i]:
        res.append(i)
        for j in range(i * i, 2000000, i):
            prime[j] = False
while t > 0:
    t -= 1
    n = int(input())
    if n in res:
        sums += n
    else:
        for i in res:
            if i > math.sqrt(n):
                break
            while n % i == 0:
                sums += i
                n /= i
            if n in res:
                sums += n
print(int(sums))
