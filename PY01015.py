t = int(input())
while t>0 :
    n = input()
    dem=0
    for i in range(len(n)-1):
        if int(n[i]) > int(n[i + 1]):
            dem+=1
            break
    if dem:
        print("NO")
    else:
        print("YES")
    t-=1
