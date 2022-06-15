s = input()
dem1, dem2 = 0, 0
for i in s:
    if i.islower():
        dem1 += 1
    elif i.isupper():
        dem2 += 1
if dem1 >= dem2:
    s = s.lower()
else:
    s = s.upper()
print(s)
