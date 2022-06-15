from collections import Counter

t = int(input())
while t > 0:
    t -= 1
    arr = []
    n = int(input())
    while n > 0:
        n -= 1
        k = int(input())
        arr.append(k)
    arr.sort()
    arr1 = Counter(arr)
    count = 0
    res = 0
    for i in arr1:
        if count < arr1[i]:
            count = arr1[i]
            res = i
    print(res)
