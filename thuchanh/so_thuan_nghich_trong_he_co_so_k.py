def convert_num(n, b):
    if n < 0 or b < 2:
        return ""
    res = ""
    t = n
    while t > 0:
        res += str(t % b)
        t = int(t / b)
    if res == res[::-1]:
        return True
    else:
        return False


n, m, k = list(map(int, input().split()))
count = 0
for i in range(n, m + 1):
    if convert_num(i, k):
        count += 1
print(count)
