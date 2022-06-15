lst = []
while len(lst) < 10:
    s = input().split()
    for i in s:
        lst.append(int(i) % 42)
mySet = set(lst)

print(len(mySet))
