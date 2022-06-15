# PERFECT PRIME
def sums(n):
    s = str(n)
    sum1 = 0
    for i in s:
        sum1 += int(i)
    return sum1


n = 1000000
prime = [True for i in range(n + 1)]
prime[0], prime[1] = False, False
l = 2
while l ** 2 <= n:
    if prime[l]:
        for j in range(l * l, n + 1, l):
            prime[j] = False
    l += 1
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    k = str(n)
    s = int(k[::-1])
    check = True
    if prime[n] and prime[s] and prime[sums(n)]:
        for y in k:
            if not prime[int(y)]:
                check = False
                break
    else:
        check = False
    if check:
        print('Yes')
    else:
        print('No')
