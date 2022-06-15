# TỔNG CHỮ SỐ - TÍCH CHỮ SỐ
t = int(input())
while t > 0:
    t -= 1
    sum = 1
    mul = 0
    count = 0
    n = input()
    for i in range(len(n)):
        if i % 2 == 0:
            if int(n[i]) != 0:
                sum *= int(n[i])
                count += 1
        else:
            mul += int(n[i])
    if count != 0:
        print(str(sum)+" "+str(mul))
    else:
        print("0 "+str(mul))
