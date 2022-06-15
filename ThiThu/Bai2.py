# swap CASE
s = input()
a = []
for i in range(len(s)):
    if s[i].islower():
        a.append(s[i].upper())
    else:
        a.append(s[i].lower())
for i in a:
    print(i, end="")
