# tích chữ số
def mul(n):
    s = str(n)
    t = 1
    for i in s:
        if int(i) != 0:
            t *= int(i)
    return t


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    print(mul(n))

