a, k, n = list(map(int, input().split()))
count = 0
res = k - a % k
for b in range(res, n - a + 1, k):
    res = a + b
    if res % k == 0:
        print(b, end=' ')
        count += 1
if count == 0:
    print(-1)
