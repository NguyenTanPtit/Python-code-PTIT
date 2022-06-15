# xác định thể thơ
t = int(input())
arr = []
dem = 0
dem1 = 0
while t > 0:
    t -= 1
    s = input().split()
    if len(s) == 7:
        dem += 1
        if dem1 > 0:
            arr.append(dem1)
            dem1 = 0
        if dem == 4:
            arr.append(7)
            dem = 0
    if len(s) == 6 or len(s) == 8:
        dem1 += 1
if dem1 > 0:
    arr.append(dem1)
print(len(arr))
for i in arr:
    if i == 7:
        print(2)
    else:
        print(1)
