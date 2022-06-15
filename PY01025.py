def dauPhay(n):
    s = str(n)
    res = ""
    count = 1
    for i in range(len(s) - 1, 0, -1):
        if count % 3 == 0:
            res += s[i]
            res += ","
            count += 1
        else:
            res += s[i]
            count += 1
    res += s[0]
    print(res[::-1])


n = int(input())
dauPhay(n)
