# gửi thông báo
t = int(input())
while t > 0:
    t -= 1
    m = input()
    if len(m) <= 100:
        print(m)
    else:
        s = list(map(str, m.split()))
        res = s[0]
        for i in range(1, len(s)):
            if len(res) + len(s[i]) + 1 <= 100:
                res += " " + s[i]
                print(len(res))
            else:
                print(res)
                break
