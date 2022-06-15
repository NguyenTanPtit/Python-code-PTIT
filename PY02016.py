import array
from collections import Counter

n = int(input())

while n > 0:
    phanTu = int(input())
    lst = array.array('i')
    n -= 1
    str = input()
    x = str.split()
    for i in x:
        lst.append(int(i))
    d = Counter(lst)
    res = 0
    dem = 0
    for i in d:
        if dem < d[i]:
            dem = d[i]
            res = i
        elif dem == d[i]:
            if res > i:
                res = i
    if dem > (phanTu / 2):
        print(res)
    else:
        print("NO")
