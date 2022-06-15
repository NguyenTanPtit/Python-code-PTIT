def convert_num(n, b):
    if n < 0 or b < 2:
        return ""
    res = ""
    t = n
    while t > 0:
        if t > 10:
            m = t % b
            if m > 10:
                res += str(chr(55 + m))
            else:
                res += str(m)
        else:
            res += str(t % b)
        t = int(t / b)
    return "".join(reversed(res))


n = int(input())
while n > 0:
    n -= 1
    a, b = list(map(int, input().split()))
    print(convert_num(a, b))
