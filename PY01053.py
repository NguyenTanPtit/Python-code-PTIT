# chia hết cho 3
def sum(n):
    s = str(n)
    sum = 0
    for i in s:
        sum += int(i)
    return sum


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    if sum(n) % 3 == 0:
        print("YES")
    else:
        print("NO")
